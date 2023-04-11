print('======CONTADOR DE NÚMEROS======')

cont=0
soma=0
print('DÍGITE OS NÚMEROS QUE DESEJA, QUANDO TERMINAR DIGITE [999] PARA SOMAR OS VALORES!')
while cont<999:
	valor=int(input ('dígite o valor: '))
	cont+=1
	soma+=valor
	if valor==999:
		print(soma-999)