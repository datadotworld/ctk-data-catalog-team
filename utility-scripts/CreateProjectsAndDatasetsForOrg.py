import json
import requests
import argparse
import os
from dotenv import load_dotenv
import time

################################################################################################
## The script is intended to create all the required projects before CTK deployment
## This is a pre-processing step that implements a missing part from dwt
################################################################################################

class CreateProjects:
	adminToken = ''
	baseURL = 'https://api.data.world/'
	# baseURL = 'https://api.mckinsey.data.world/'
	# baseURL = 'https://api.verisk.data.world/'
	
	data_catalog_team = 'data-catalog-team'

	main = 'main'
	ctk_data_catalog_team_projects = [
		'DDW Metrics Etl Solutions'
	]

	required_datasets = [
		"DDW Catalogs"
	]
	agentIdPrefix = ''

	def __init__(self, agentId):
		load_dotenv()
		self.adminToken = os.environ.get('CUSTOMER_API_TOKEN')
		self.configFileName = os.environ.get('CUSTOMER_DATA_CATALOG_TEAM')
		self.data_catalog_team_name = self.configFileName.split('-',1)[1]

		self.apiURL = os.environ.get('PRIVATE_INSTANCE_CUSTOMER_API_URL')

		if 'mckinsey' in self.apiURL.lower():
			self.baseURL = 'https://api.mckinsey.data.world/'

		# In some use cases, customer has a slug for catalog config such as so the prefix does not match the catalog config org agent id such as solutions-catalog-config vs solutions-training-catalog-config. In this scenario, we take the slug and add to `catalog-config` and `catalog-sources`
		if self.data_catalog_team_name != 'data-catalog-team':
			self.setNames(self.data_catalog_team_name)
			
		# Calling function to create projects
		self.createProject(self.data_catalog_team, self.ctk_data_catalog_team_projects)
	
	def update_dataset_title(self, org, dataset, title):
		print(f"Updating {org}/{dataset} title to {title}")
		requestHeaders= {
			'Accept': 'application/json',
			'Authorization': 'Bearer {}'.format(self.adminToken),
			'Content-Type': 'application/json'
		}

		requestUrl = f'{self.baseURL}v0/datasets/{org}/{dataset}'

		requestJSON= {
			"title": title
		}
		print(f'Calling {requestUrl} to update {dataset} title')
		requestBody = json.dumps(requestJSON)
		response = self.callAPIEndpoint(requestUrl, requestBody, requestHeaders, callType='patch')

		print(response)
		if response.status_code == 200:
			print(response.json()["message"])
		else:
			print(response.json()["message"])
	
	# Create data source datasets for additional org
	# This dataset is intended to store collector output file of additional customer org
	def preprocess_datasets(self, arr, keyword, org):
		datasets = []
		for item in arr:
			if keyword in item:
				value = item.replace(keyword, "").strip()
				new_item = f"{value} {org.title()}"
				datasets.append(new_item)
		return datasets

	def setNames(self, agentId) -> None:
		if agentId:
			self.data_catalog_team = agentId

	def loadCredentials(self, credentialsFile):
		with open(credentialsFile, 'r') as data_file:
			credentials = json.load(data_file)
		return credentials

	def getAdminToken(self, credentialFile):
		credentials = self.loadCredentials(credentialFile)
		return credentials['adminToken']

	def callAPIEndpoint(self, reqURL, reqBody, reqHeader, callType):
		# Adding 25ms delay to avoid 429 Too many requests response from server
		time.sleep(0.25) 
		if callType == 'get':
			response = requests.get(
				reqURL,
				headers=reqHeader
			)
			return response
		elif callType == 'post':
			response = requests.post(
				reqURL,
				data=reqBody,
				headers=reqHeader
			)
			return response
		elif callType == 'patch':
			response = requests.patch(
				reqURL,
				data=reqBody,
				headers=reqHeader
			)
			return response

	def checkIfDatasetIsCreated(self, org):
		requestHeaders= {
			'Authorization': 'Bearer {}'.format(self.adminToken),
			'Content-Type': 'application/json'
		}

		requestUrl = f'{self.baseURL}v0/datasets/{org}?limit=100'
		response = self.callAPIEndpoint(requestUrl, None, requestHeaders, callType='get')
		datasets = []
		if response.status_code == 200:
			for record in response.json()["records"]:
				if "id" in record:
					datasets.append(record["id"])
		else:
			print(response.json())
		
		return datasets

	def createDataset(self, org, datasets):
		requestHeaders= {
			'Authorization': 'Bearer {}'.format(self.adminToken),
			'Content-Type': 'application/json'
		}

		temp_datasets = self.checkIfDatasetIsCreated(org)
		requestUrl = f"{self.baseURL}v0/datasets/{org}"
		duplicate_datasets = []
		for dataset in datasets:
			temp_dataset = dataset.lower().replace(' ', '-')
			try:
				if temp_datasets:
					if temp_dataset in temp_datasets:
						print(f"Dataset: {dataset} already created in {org}.")
						duplicate_datasets.append(dataset)
				else:
					raise Exception(f'{org} does not have any dataset')
			except Exception as e:
				print(f"Error: {e}")
		_datasets = datasets
		
		if _datasets:
			for dataset in _datasets:
				if dataset in duplicate_datasets:
					pass
				elif 'user layer' in dataset.lower():
					pass
				elif 'column statistics' in dataset.lower():
					pass
				else:
					self.createAssetHelper(dataset, requestUrl, requestHeaders)

	def createAssetHelper(self, assetId, requestUrl, requestHeaders):
		requestJSON= {
			"title": assetId,
			"license": "ODC-ODbL",
			"visibility": "PRIVATE"
		}
		print(f'Calling {requestUrl} to create {assetId}')
		requestBody = json.dumps(requestJSON)
		response = self.callAPIEndpoint(requestUrl, requestBody, requestHeaders, callType='post')

		if response.status_code == 200:
			print(response.json()["message"])
		else:
			print(response.json()["message"])
		
	def checkIfProjectIsCreated(self, org):
		requestHeaders= {
			'Authorization': 'Bearer {}'.format(self.adminToken),
			'Content-Type': 'application/json'
		}

		requestUrl = f'{self.baseURL}v0/projects/{org}?limit=100'
		response = self.callAPIEndpoint(requestUrl, None, requestHeaders, callType='get')
		projects = []
		if response.status_code == 200:
			for record in response.json()["records"]:
				if "id" in record:
					projects.append(record["id"])
		else:
			print(response.json())
		return projects

	def createProject(self, org, projects): 
		requestHeaders= {
			'Authorization': 'Bearer {}'.format(self.adminToken),
			'Content-Type': 'application/json'
		}

		temp_projects = self.checkIfProjectIsCreated(org)
		requestUrl = f"{self.baseURL}v0/projects/{org}"
		duplicate_projects = []
		for project in projects:
			temp = project.lower().replace(' ', '-')
			try:
				if temp_projects:
					if temp in temp_projects:
						print(f"Data project: {project} already created in {org}.")
						# Append project name that's already created
						duplicate_projects.append(project)
				else:
					raise Exception(f'The org does not have any project')
			except Exception as e:
				print(f"Error: {e}")	

		if projects:
			for project in projects:
				if project in duplicate_projects:
					pass
				else:
					self.createAssetHelper(project, requestUrl, requestHeaders)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	# credentials file location
	# parser.add_argument('-f', '--file', help='file path of the credential file', required=True)
	# agentId prefix such as 8bank for 8bank-catalog-config
	parser.add_argument('-a', '--agentid', help='the agentID prefix of the org', required=False)
	args = parser.parse_args()
	# credentials = args.file
	agentId = args.agentid

	# T = CreateProjects(credentials, agentId)
	T = CreateProjects(agentId)
	# print(T.adminToken)
	# print(T.catalog_sources)