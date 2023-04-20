#exercicio 107
def dobro(x, moeda = False):
	x= x * 2
	if moeda: # ex109
			x = f'R${x:.2f}'
	return x
	
def metade(x, moeda = False):
	x = x/2
	if moeda:  #ex109
		x = f'R${x:.2f}'
	return x
	
def aumenta(x, y, moeda = False):
	x = (x * y /100) + x
	if moeda: #ex109
		x = f'R${x:.2f}'
	return x

def diminui(x, y, moeda = False):
	x = x - (x * y/100 )
	if moeda: #ex109
		x = f'R${x:.2f}'
	return x

#exercicio 108

def moeda(x):
	x = (f'R${x:.2f}')
	return x
	
	
#exercicio 110

def resumo(x, y, z):	
	print(f'''{'-'*25}
     resumo do valor
{'-'*25}
preço informado:         R${x:.2f}
dobro do preço:          R${x * 2:.2f}
metade do preço:         R${x / 2:.2f}
{y}% de aumento:          R${x + (x * y / 100):.2f}
{z}% de diminuição:       R${x - (x * z /100 ):.2f}
{'-'*25}''')
	