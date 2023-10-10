import json
import requests

import datetime
from datetime import timezone, timedelta
import argparse
import os

class ServiceToken:
    adminToken = ''
    serviceToken = ''
    expiryDate = ''
    # Base URL for PI and MT
    baseURL = 'https://api.data.world/'
    # Base URL for Verisk VPC
    # baseURL = 'https://api.verisk.data.world/'
    # baseURL = 'https://api.mckinsey.data.world/'
    # Desired username suffix for catalog config
    # e.g. sa-datadotworld-cc
    desiredUsername = 'coresupport'
    displayName = ''

    def __init__(self, credentialFile, agentId, hours):
        self.displayName = "SA DDW Support"
        self.adminToken = self.getServiceToken(credentialFile,agentId, hours)

    def loadCredentials(self, credentialsFile):
        with open(credentialsFile, 'r') as data_file:
            credentials = json.load(data_file)
        return credentials

    def getAdminToken(self, credentialFile):
        credentials = self.loadCredentials(credentialFile)
        self.adminToken = credentials['adminToken']

    def getExpiryDate(self, hours):
        # Create a UTC timestamp 24 hours from now
        dt = datetime.datetime.now(timezone.utc) + timedelta(hours=hours)
        self.expiryDate = dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        # print(self.expiryDate)

    def callAPIEdnpoint(self, reqURL, reqBody, reqHeader):
        response = requests.post(
            reqURL,
            data=reqBody,
            headers=reqHeader
        )
        return response

    def getServiceToken(self, credentialFile, agentId, hours):
        self.getAdminToken(credentialFile)
        self.getExpiryDate(hours)
        requestHeaders= {
            'Authorization': 'Bearer {}'.format(self.adminToken),
            'Content-Type': 'application/json'
        }

        requestUrl = self.baseURL + 'v0/serviceaccount/' + agentId

        # requestBody = '''
        # {
        #     "desiredUsername": "%s",
        #     "expiryDate" : "%s"
        # }
        # ''' % desiredUsername, 
        print("test "+ self.displayName)
        requestJSON = {
            "desiredUsername": self.desiredUsername,
            # "expiryDate" : self.expiryDate,
            "displayName": self.displayName
        }

        requestBody = json.dumps(requestJSON)
        
        response = self.callAPIEdnpoint(requestUrl, requestBody, requestHeaders)
        
        responseData = response.json()
        print("Response data %s \n" %responseData)
        if response.status_code == 200:
            response = response.json()
            self.serviceToken = response['token']
            # print(response['token'])
        elif responseData['message'] == 'Username already exists':
            # print("%s \n" % responseData['message'])
            print("Refreshing the token \n")
            requestBody = '''
            {
                "expiryDate" : "%s"
            }
            ''' % self.expiryDate
            requestUrl = self.baseURL + 'v0/serviceaccount/' + 'sa-' + agentId + '-' +self.desiredUsername + '/refresh' 
            
            response = self.callAPIEdnpoint(requestUrl, requestBody, requestHeaders)

            response = response.json()
            print("Refreshing token response %s \n" % response)
            self.serviceToken = response['token']
            print("This Service Account token would expire by %s \n" % self.expiryDate)
        elif response.status_code == 400 | response.status_code == 404 :
            print("HTTP Status Code %i \n" % response.status_code)
            print("%s \n" % responseData['message'])
        else :
            print("HTTP Status Code %i \n" % response.status_code)
            # print("%s \n" % responseData)
            print("%s \n" % responseData['message'])

        # print(response.json())
        # Verify if a service token already exist for the username 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # credentials file location
    parser.add_argument('-f', '--file', help='file path of the credential file', required=True)
    # agentId
    parser.add_argument('-a', '--agentid', help='the agentID of the org', required=True)
    # hours to expire
    parser.add_argument('-t', '--time', default=1, help='time to expire the token in hours', required=False)
    args = parser.parse_args()
    credentials = args.file
    agentId = args.agentid
    hours = int(args.time)
    
    T = ServiceToken(credentials, agentId, hours)
    if  T.serviceToken == "" :
        print("No token is populated\n") 
    else: 
        print("The Service Account token for org %s is \n%s\n" % (agentId, T.serviceToken))
    print("Execute the the below shell command in terminal\n")
    commandLine = "export " + "DW_AUTH_TOKEN="+T.serviceToken
    print(commandLine)
    os.system(commandLine)
    # commandLine2 = "source ~/.zshrc"
    # os.system(commandLine2)
    print("\nComplete!")