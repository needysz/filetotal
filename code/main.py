import os
from sys import exit 

class dub:
	def dubbing():
		files = os.listdir()
		for dirfile in files:
			cleanfile = open(dirfile, 'w')
			cleanfile.close()

	def dubbing_filelist():
		files = os.listdir()
		print('INFO:\n')
		for dirfiles in files:
			cleanfile = open(dirfiles, 'r')
			if os.path.getsize(dirfiles) > 0:
				print(dirfiles, '- ERROR: NOT CLEANED')
			elif os.path.getsize(dirfiles) == 0:
				print(dirfiles, '- REPORT: CLEANED')
			cleanfile.close()

os.system('cls')											# Авторство
print('\n$ FileTotal : Alpha 0.1\n$ AUTHOR : by @needy_sz\n')						# 

act = str(input('$> '))											# Выбор режима

if act == 'mode dub' or act == 'dub mode':								# dubbing-mode
	print('<DUBBING MODE>')

	path = input('\n$> path: ')

	try
		os.chdir(path)										# Переход по указанному пути
	except FileNotFoundError:
		print('\nERROR: [ INVALID PATH ]')
		exit()

	files = os.listdir()										# Присваивание переменной   

	print('''
   @  PATH: {0}
   @ FILES: {1}
   @  ACTS: {2}
		'''.format( path, files, '"start dub / undo"' ) )

	act = str(input('$> '))

	if act == 'start dub':
		dub.dubbing()
		print('\n[ DUBBING PROCESS HAS BEEN ENDED ]\n')
		dub.dubbing_filelist()

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
	print('\nERROR: [ INVALID MODE ]\n')
	exit()
