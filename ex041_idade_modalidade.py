from datetime import date
#ano atual
ano=date.today().year
#ano de nascimento
nascimento= int(input('qual seu ano de nascimento? '))
idade=ano-nascimento
if idade <= 9:
	print(f'voce tem {idade} anos, sua modalidade é MIRIM! ')
elif idade <= 14:
	print(f'voce tem {idade} anos, sua modalidade é INFANTIL!')
elif idade <= 19:
	print(f'voce tem {idade} anos, sua modalidade é JUNIOR!')
elif idade <= 25:
	print(f'voce tem {idade} anos, sua modalidade é SENIOR! ')
else:
	print(f'voce tem {idade} anos, sua modadelidade é MASTER! ')