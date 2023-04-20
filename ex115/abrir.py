def abrirarquivo(nome):
	try:
		a = open(nome, 'rt')
		a.close()
	except:
		print (f'o arquivo {nome} não foi encontrado ')
		criararquivo(nome)
		return False
	else:
		return True 
	

def criararquivo(nome):
	a = open(nome, 'wt+')
	a.close()
	print(f'o arquivo {nome} foi criado com sucesso!')
	
	
def lerarquivo(nome):
	try:
		a = open(nome, 'rt')
	except:
		print('ERRO AO ABRIR O ARQUIVO!')
	else:
		for linha in a:
			dado = linha.split(';')
			dado[1] = dado[1].replace('\n', '')
			print(f'{dado[0]:.<30} {dado[1]:>3} anos')
def leiaint(z):
	x=input(z)
	while True:
		if x.isnumeric():
			break
		else:
			print ('\033[1;31mnúmero inválido! \033[m')
			x = input('dígite um número válido: ')
	
	return int(x)
		
	
def cadastrar(arq, nome='desconhecido', idade=0):
	try:
		a = open(arq, 'at')
	except:
		print('ouve um erro na abertura do arquivo! ')
	else:
		try:
			a.write(f'{nome};{str(idade)}\n')
		except:
			print('ouve um erro ao escrever o arquivo! ')
		else:
				print(f'o cadastro de {nome} foi adicionado! ')
				a.close()