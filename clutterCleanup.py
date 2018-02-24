import os
from os import listdir
from os.path import isfile, join
import sys

if (os.name == 'nt') :
	rootdir = os.path.join(os.environ['USERPROFILE'])
	sourcePath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + "\\"
	destinationPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents') + "\\"
elif (os.name == 'posix') :
	rootdir = os.path.join(os.path.expanduser('~'))
	sourcePath = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') + "/"
	destinationPath = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') + "/"

fileList = []
fileNamefileSizeList = []

for root, subFolders, files in os.walk(rootdir) :
	for file in files :
		f = os.path.join(root, file)
		fileList.append(f)
		try :
			fileNamefileSizeList.append(tuple([f, os.path.getsize(f)/1024.0/1024.0]))
		except OSError :
			pass

fileNamefileSizeList.sort(key = lambda x: x[1], reverse = True)

counter = 0

for a, b in fileNamefileSizeList :
	counter = counter + 1
	print(counter, " ", a, " - ", b)
	if counter == 10 :
		break

onlyfiles = [f for f in listdir(sourcePath) if isfile(join(sourcePath, f))]
temp = [os.path.splitext(sourcePath + file) for file in onlyfiles]
extensionList = [x[1] for x in temp]
uniqueExtensionList = list(set(extensionList))

ignoreExtensionList = ['.lnk']

for currIgnore in ignoreExtensionList :
	if currIgnore in uniqueExtensionList :
		uniqueExtensionList.remove(currIgnore)

for currExten in uniqueExtensionList :
	currExtension = currExten[1:]
	if not os.path.exists(destinationPath + currExtension) :
		os.makedirs(destinationPath + currExtension)

for file in onlyfiles :
	k = file.rfind(".")
	moveFolder = file[(k + 1):]
	m = file.find("\\")
	oldFile = file[(m + 1):]
	n = file.rfind("\\")
	newFile = file[(n + 1):]
	if os.path.exists(destinationPath + moveFolder) :
		os.rename(sourcePath + oldFile, destinationPath + moveFolder + "/" + newFile)