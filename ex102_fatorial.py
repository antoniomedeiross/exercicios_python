from math import factorial

def fatorial(x, show = False):
	f = factorial(x)
	if show == True:
		for c in range (x, 0, -1):
			if c > 1:
				print( c,'×', end= ' ')
			else:
				print(c, '=', end=' ')
	return f
#se quiser ver o passo a passo do cálculo insira True nós argumentos	
print(fatorial(5,True))
	