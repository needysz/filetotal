import os
from sys import exit

def dubbing():
	files = os.listdir()
	for dirfile in files:
		delfile = open(dirfile, 'w')
		delfile.close()

def dubbing_filelist():
	files = os.listdir()
	print('INFO:\n')
	for dirfiles in files:
		print(dirfiles + ' - CLEANED')

os.system('cls')												# Авторство
print('\n$ FileTotal : Alpha 0.1\n$ AUTHOR : by @needy_sz\n')	# 

act = str(input('$> '))

if act == 'mode dub' or act == 'dub mode':		# dubbing-mode
	print('<DUBBING MODE>')

	
	path = str(input('\n$> path: '))

	try:
		os.chdir(path)			# Переход по указанному пути
	except FileNotFoundError:
		print('\nERROR: [ INVALID PATH ]')
		exit()

	files = os.listdir()	# Присваивание переменной   

	print('''
   @  PATH: {0}
   @ FILES: {1}
   @  ACTS: {2}
		'''.format( path, files, '"start dub / undo"' ) )


	act = str(input('$> '))

	if act == 'start dub':
		dubbing()
		print('\n[ DUBBING PROCESS HAS BEEN ENDED ]\n')
		dubbing_filelist()

	elif act == 'undo' or 'undo()':
		exit()

	elif act == 'exit' or 'exit()':
		exit()

	else:
		print('\nERROR: [ INVALID COMMAND ]\n')
		exit()

elif act == 'exit' or 'exit()':
	exit()

else:
	print('\nERROR: [ INVALID COMMAND ]\n')
	exit()
