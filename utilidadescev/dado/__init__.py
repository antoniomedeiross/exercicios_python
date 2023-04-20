def leia(x):
	x=x.replace(',', '.')
	while not (x.isdigit() or (x.count('.') == 1 and x.replace('.', '').isdigit())):
	
		print('ERRO! INFORME UM NÚMERO VÁLIDO!')
		x = input('digite novamente: ')
	
	return float(x)



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
	