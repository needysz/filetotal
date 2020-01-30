import os
from sys import exit

os.system('cls')
print('\n$ FileTotal : Alpha 0.1\n$ AUTHOR : by @needy_sz\n')

def quit():
	os.system('cls')
	os.system('cmd')
	exit()

def dubbing():
	files = os.listdir()
	for dirfile in files:
		delfile = open(dirfile, 'w')
		delfile.close()

def dubbing_fileslist():
	files = os.listdir()
	print('INFO:\n')
	for dirfiles in files:
			print(dirfiles + ' - CLEANED')

try:
	act = str(input('$> '))
except TypeError:
	print('\nERROR: [ INVALID COMMAND ]\n')
	exit()

if act == 'mode dub':		# dubbing-mode
	print('<DUBBING MODE>')

	try:	
		path = str(input('\n$> path: '))
	except TypeError:
		print('\nERROR: [ INVALID PATH ]\n')
		exit() 

	os.chdir(path)			# Переход по указанному пути
	files = os.listdir()	# Присваивание переменной 

	print('''
   @  PATH: {0}
   @ FILES: {1}
   @  ACTS: {2}
		'''.format( path, files, '"start dub / undo"' ) )

	try:
		act = str(input('$> '))
	except TypeError:
		print('\nERROR: [ INVALID COMMAND ]\n')
		exit()

	if act == 'start dub':
		dubbing()
		print('\n[ DUBBING PROCESS HAS BEEN ENDED ]\n')
		dubbing_fileslist()

	elif act == 'undo':
		quit()

elif act == 'exit':
	quit()

else:
	print('\nERROR: [ INVALID COMMAND ]\n')
	exit()
