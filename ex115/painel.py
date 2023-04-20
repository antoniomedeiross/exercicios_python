def painel():
	print(f'''{'-'*50}
{'MENU PRINCIPAL':^50}
{'-'*50}
 1→ \033[35mver pessoas cadastradas\033[m
 2→ \033[35mnovo cadastro\033[m
 3→ \033[35msair\033[m
 {'-'*50}''')
	while True:
		try:
			x=int(input('sua escolha: '))
			if 0< x <4:
				break
			else:
				print('\033[31mINFORME UM NÚMERO VÁLIDO!\033[m')
				continue
		except:
			print('\033[31mINFORME UM NÚMERO VÁLIDO!\033[m')		
	
	return x

def cabecalho(n):
	print('-'*40)
	if n == 1:
		print('PESSOAS CADASTRADAS'.center(40))
	elif n == 2:
		print('NOVO CADASTRO'.center(40))
	elif n == 3:
		print('SAINDO'.center(40))
	print('-'*40)
	
	
