def dobro(x, moeda = False):
	x= x * 2
	if moeda: 
			x = f'R${x:.2f}'
	return x
	
def metade(x, moeda = False):
	x = x/2
	if moeda:  
		x = f'R${x:.2f}'
	return x
	
def aumenta(x, y, moeda = False):
	x = (x * y /100) + x
	if moeda: 
		x = f'R${x:.2f}'
	return x

def diminui(x, y, moeda = False):
	x = x - (x * y/100 )
	if moeda: 
		x = f'R${x:.2f}'
	return x



def moeda(x):
	x = (f'R${x:.2f}')
	return x
	