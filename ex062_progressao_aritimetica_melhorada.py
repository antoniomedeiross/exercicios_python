print('PROGRESSAO ARITIMETICA!')
termo=int(input('informe o primeiro termo: '))
razao=int(input('informe a razão: '))
cont=0
pro=0
while cont != 10:
	
	print(termo, end=' ')
	print('-->' if cont < 9 else '.', end= ' ')
	cont+=1
	termo+=razao

mais=int(input('\ndeseja mais números? quantos?\n[0] Para finalizar!'))

cont2=0
while cont2 != mais:
	print(termo, end=' ')
	termo+=razao
	cont2+=1