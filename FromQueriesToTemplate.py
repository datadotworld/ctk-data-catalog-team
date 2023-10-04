import os
import sys
import traceback
import re

class Transformer:
	queryFile = ''
	
	def __init__ (self, queryFile, projectLocation):
		self.readTemplate(queryFile, projectLocation)

	def transformFile(self, queryFile):
		output = ''
		with open(queryFile, 'r') as f:
			lines = f.readlines()
			for line in lines:
				# print('test')
				output = output + repr(line)[1:-1]
		return (output.replace('"', '\\"'))

	def readTemplate(self, file, template):
		path, name = os.path.split(file)

		fileFound = False

		if not os.path.exists(template):
			raise Exception("Selected path does not exist: " + template)

		with open(template, 'r+') as f:
			newlines = []
			flag = False
			newContent = ''
			lines = f.readlines()
			for i in range(0, len(lines)):
				line = lines[i]
				title = re.findall(r'"(.*?)(?<!\\)"', line)
				if 'dct:title' in line and name == title[0]:
					if flag == False:
						newlines.append(line)
						newContent = '\tdwt:content  "' + self.transformFile(file) + '" ;\n'
						flag = True
						fileFound = True
				elif flag == True:
					newlines.append(newContent)
					flag = False
				elif flag == False:
					newlines.append(line)
					flag = False
		
		if fileFound:
			try:
				with open(template, 'w') as f:
					for line in newlines:
						f.write(line)
			except:
				print('ERROR: Cannot open/access existing file for writing: ' + template)


if __name__ == '__main__':
	
	try:
		DEFAULT_PATH = '.'

		if len(sys.argv) < 2:
			queryLocation = DEFAULT_PATH
			templateLocation = DEFAULT_PATH
		elif len(sys.argv) < 3:
			queryLocation = DEFAULT_PATH
			templateLocation = sys.argv[1]
		else:
			queryLocation = sys.argv[1]
			templateLocation = sys.argv[2]
		
		patterns = ['']

		if not os.path.exists(queryLocation):
			raise Exception("Selected path does not exist: " + queryLocation)
		
		# Walks through directory structure looking for files matching patterns
		matchingFileList = \
			[os.path.join(dp, f) \
				for dp, dn, filenames in os.walk(queryLocation) \
					for f in filenames \
						if os.path.splitext(f)[1] in patterns]

		print('Files found matching patterns: ' + str(len(matchingFileList)))

		template = ['template']

		# Walks through directory and search for the template
		templateFileList = \
			[os.path.join(dp, f) \
				for dp, dn, filenames in os.walk(templateLocation) \
					for f in filenames \
						if os.path.splitext(f)[0] in template]

		fileCount = 0
		filesReplaced = 0

		for currentFile in matchingFileList:
			print(currentFile)
			fileCount+=1
			# print(currentFile + '\n')
			for temp in templateFileList:
				fileReplaced = Transformer(currentFile, temp)
				if fileReplaced:
					filesReplaced+=1
		
		# print("%s files found with .rq file extension \n" % fileCount)
		if fileCount > 1:
			print("%s files in the directory %s \n" % (fileCount, queryLocation))
		else:
			print("%s file in the directory %s \n" % (fileCount, queryLocation))
	
	except Exception as err:
		print(traceback.format_exception_only(type(err), err)[0].rstrip())
		sys.exit(-1)