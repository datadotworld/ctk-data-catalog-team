import os
import sys
import traceback
import re
from rdflib import Graph

def usage():
	print('Extract SQL queries from template.ttl into human readable texts')

def parseStringToFile(path, fileName):

	if not(os.path.isfile(fileName) and os.access(fileName, os.W_OK)):
		print("WARNING: Skipping...File does not exist or and is not writeable:" + fileName)
		return False


	g = Graph()

	g.parse(fileName, format='turtle')

	qres = g.query(
		'''
		SELECT ?title ?content ?owner
		WHERE {
			?IRI a dwt:SqlQuery ;
				dct:title ?title ;
				dwt:content ?content ;
				dwt:owner ?owner .
		}
		'''
	)

	for title, content, owner, *_ in qres:
		# Remove prefix
		if 'project' in owner:
			owner = re.sub(r'^.*?project', 'project', owner)
		elif 'dataset' in owner:
			owner = re.sub(r'^.*?dataset', 'dataset', owner)
		# Create/Retrieve parent directory location
		parentDirLocation = createDir(path, owner)

		# Create file if the parent directory location exists
		if(parentDirLocation):
			print(parentDirLocation)
			fileName = parentDirLocation+'/'+title.value
			with open(fileName, 'w') as query_file:
				print("File Name:\n%s" % title.value )
				query_file.write(content.value)
				print('Successfully wrote the content to the file\n')


def createDirHelper(dirCreated, owner, path):
	# Create directory based on new line 
	if dirCreated:
		print("Parent Directory Path: ")
		# Create temporary dir path and remove potential unidentified and \n characters
		temp_path = (path + '/' + f'{owner}').encode('utf-8').strip().decode('utf-8')
		os.makedirs(temp_path, exist_ok=True)
		# print("%s" % temp_path)
		return temp_path

def createDir(path, owner):

	if not(os.path.exists(path) and os.access(path, os.W_OK)):
		print("WARNING: Skipping...File does not exist or and is not writeable:" + path)
		return False
	
	dirCreated = False

	owners = []
	if owner not in owners:
		dirCreated = True
		owners.append(owner)
		file_path = owner + '_queries'
		return createDirHelper(dirCreated, file_path, path)
	else:
		dirCreated = False
		return path + '/' + owner + '_queries'

def main():

	try:

		DEFAULT_PATH = '.'
		if len(sys.argv) < 2:
			usage()
			path = DEFAULT_PATH
		else:
			path = sys.argv[1]

		usage()
		print('[Directory To Check] : ' + path)

		patterns = ['template.ttl']
		# names = ['template.ttl']
		name = 'template.ttl'
		if not os.path.exists(path):
			raise Exception("Selected path does not exist: " + path)

		matchingFileList =  []
		for root, dirs, files in os.walk(path):
			if name in files:
				matchingFileList.append(os.path.join(root, name))
		
		print('Files found matching patterns: %s \n' % str(len(matchingFileList)))

		for currentFile in matchingFileList:
			parseStringToFile(path, currentFile)

	except Exception as err:
		print(traceback.format_exception_only(type(err), err)[0].rstrip())
		sys.exit(-1)

if __name__ == '__main__':
	main()