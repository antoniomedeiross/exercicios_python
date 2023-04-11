from random import sample
from time import sleep
numeros = []

def sorteia(x):
	lst = sample(range(0,10),5)
	for a in lst:
		x.append(a)
		sleep(0.5)
		print(a, end=' ', flush = True)
	print('Pronto!')
	
def soma_par(x):
	soma = 0
	for a in x:
		if a % 2 == 0:
			soma += a
	print(f'a soma dos números pares de {x} foi: {soma}')
	
	
	
sorteia(numeros)
soma_par(numeros)