from datetime import date

def voto(x):
	idade = date.today().year - x 
	
	if 15 < idade < 18:
		a = f'voce tem {idade} anos, o voto é opcional '
	elif idade < 16:
		a = f' voce tem {idade} anos, ainda não pode votar' 
	elif 18 <= idade < 65:
		a = f'voce tem {idade} anos, o voto é obrigatório '
	else:
		a = f'vc tem {idade} anos, o voto é opcional'			
	return a


x = int(input('qual ano de nascimento: '))
print (voto(x))