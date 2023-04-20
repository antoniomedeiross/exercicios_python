from painel import *
from abrir import *
from time import sleep 
arq='cadastro.txt'

abrirarquivo(arq)
while True:
	a = painel()
#pessoas cadastradas 
	if a == 1:
		sleep(0.5)
		cabecalho(a)
		lerarquivo(arq)
		sleep(1.5)
#novo cadastro
	elif a == 2:
		sleep(0.5)
		cabecalho(a)
		nome = input('nome: ')
		idade = leiaint('idade: ')
		cadastrar(arq, nome, idade)
		sleep(1.5)
#sair
	elif a == 3:
		sleep(0.5)
		cabecalho(a)
		sleep(1.5)
		print('programa encerrado!')
		break
