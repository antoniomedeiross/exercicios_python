num= int(input('dígite um número: '))
cont=0
for c in range(1, num +1):
	if num % c == 0:
		print('\033[32m',c ,'\033[m', end=' ')
		cont += 1
	else:
		print('\033[31m', c , '\033[m',end=' ')
	if cont == 2:
		primo='é' 
	else:
		primo='não é'
print (f'\no número {num} {primo} primo, pois é divisivel por {cont} números')
	