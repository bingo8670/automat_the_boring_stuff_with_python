import os

os.chdir('E:\\')
for folderName, subfolders, filenames in os.walk('E:\\'):
	current = os.path.abspath('.')

	for filename in filenames:
		name = folderName + '\\' + filename
		size = os.path.getsize(name)
		size = size / 1024 / 1024
		if size > 100:
			print('The current folder is ' + folderName)
			print('The file that beyond 100MB is: ' + name)
