from time import sleep

def titulo(x):
	print('='*40)
	print(x)
	print('='*40)
	
	
def c_regressiva(a, b, c):
	sleep(0.5)
	titulo(f'contagem de {a} até {b} de {c} em {c}')
	if c == 0:
		c=1
	if a < b:
		for l in range (b):
			sleep(0.5)
			print(a, end= ' ', flush=True)
			a += c
			if a > b:
				break
		print('FIM!')
	elif c < 0:
		while not a < 0:
			sleep(0.5)
			print(a, end=' ', flush=True)
			a+=c
		print('FIM!')
		
	else:
		for l in reversed(range (a)):
			sleep(0.5)
			print(a, end= ' ', flush=True)
			a += -c
			if a < 0:
				break
		print('FIM!')
c_regressiva(1, 10, 1)
print()
c_regressiva(10, 1, 2)
print()
sleep(0.5)
titulo('agora faça a sua própria contagem')

a = int(input('inicio: '))
b = int(input('fim: '))
c = int(input('passo: '))

c_regressiva(a, b, c)