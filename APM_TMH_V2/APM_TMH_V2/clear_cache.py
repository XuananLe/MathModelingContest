import shutil
import os

file_name = 'APM_TMH_V2'

# shutil.rmtree(file_name + '.aux')
# shutil.rmtree(file_name + '.log')
# shutil.rmtree(file_name + '.out')
# shutil.rmtree(file_name + '.toc')

try:
	os.remove(file_name + '.aux')
	os.remove(file_name + '.log')
	os.remove(file_name + '.out')
	os.remove(file_name + '.toc')

	print('removed')
except:
	print('no file removed')