km=float(input('qual a distância em km a ser percorrida? '))
if km > 200:
	print('a viagem custará R$' , km*0.45)
else:
	print('a sua viagem custará R$' , km*0.50)
	