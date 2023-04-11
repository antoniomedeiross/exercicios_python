print('PROGRESSAO ARITIMETICA!')
termo=int(input('informe o primeiro termo: '))
razao=int(input('informe a razão: '))
cont=0
pro=0
print('os 10 primeiros termos da p.a informada são:')
while cont != 10:
	
	print(termo, end=' ')
	print('-->' if cont < 9 else '.', end= ' ')
	cont+=1
	termo+=razao