c = ['\033[m', '\033[41m','\033[42m','\033[30m']



def ajuda(fun):
	titulo(f'manual da funcionalidade \'{fun}\'', 2 )

	print('\033[m')
	print('\033[7;31m', end =' ')
	help(fun)
	print (c[0], end= ' ')
	
	
def titulo(msg, cor):
	print(c[cor], end=' ')
	print('≈'* (len(msg)+4))
	print(f'  {msg}')
	print('≈'*(len(msg)+4))
	print(c[0], end=' ')
	
	
	

	
while True:
	titulo('SISTEMA DE AJUDA', 1)
	comando = input ('função ou biblioteca: ')
	if comando.upper() == 'FIM':
		break
	else:
		ajuda(comando)
	
print('ATE MAIS!')