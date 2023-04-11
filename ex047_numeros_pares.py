print('escolha o intervalo que deseja descobrir os números pares')
a=int(input('escolha um número PAR para iniciar: '))
b=int(input('escolha o número final: '))
print(f'os números pares entre {a} e {b} são: ')
for c in range(a, b):
	if c % 2==0:	
		print(c)