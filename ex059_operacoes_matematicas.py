n1= float(input('informe o número desejado: '))
n2=int(input('mais um: '))
op=0
while op != 5:
	print('''você deseja:
	[1] SOMAR
	[2] MULTIPLICAR
	[3] DIVIDIR
	[4] NOVOS VALORES
	[5] SAIR''')
	op=int(input('qual sua opção: '))
	
	
	if op==1:
		print(n1+n2)
				
	elif op == 2:
		print(n1*n2)
	elif op == 3:
		print(n1/n2)
	elif op == 4:
		print('informe os números novamente:')
		n1=int(input('informe o 1º número: '))
		n2= int(input('informe o 2º número: '))
if op==5:
	print('FIM')