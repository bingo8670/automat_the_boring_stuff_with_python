import os,shutil

#第一个参数是目录名，第二个参数是要复制的文件后缀名
def copyFile(folder,extname):
	for foldername,subfolder,filenames in os.walk(folder):
		for filname in filenames:

			#判断是否符合后缀规则，不符合就跳过
			if not filname.endswith(extname):
				continue

			#合成绝对路径
			absfilename = os.path.join(foldername,filname)
			print('Adding %s......'%(absfilename))

			#复制文件
			shutil.copy(absfilename,'d:\\360dat')

copyFile('d:\\Program Files (x86)\\360','.dat')
