def leiaint(x=input ('dígite um número: ')):
	while True:
		if x.isnumeric():
			print ( f'\033[1;32mvocê dígitou o número {x} \033[m' )
			break
		else:
			print ('\033[1;31mnúmero inválido! \033[m')
			x = input('dígite um número válido: ')
		

leiaint()