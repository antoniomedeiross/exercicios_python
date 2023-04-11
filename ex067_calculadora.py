print('='*5 ,'CALCULADORA','='*5)
n=0

while True:
	n=int(input('qual número deseja multiplicar? (0) para encerrar: '))
	if n == 0:
			break
	for c in range (1, 11):
		print(f'{n} x {c} = {n*c}')

print('A CALCULADORA FOI ENCERRADA, ATÉ MAIS! ')