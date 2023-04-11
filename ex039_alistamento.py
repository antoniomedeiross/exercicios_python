from datetime import date
ano=date.today().year
qual=int(input('em que ano vc nasceu: '))
falta=ano-qual-18
if ano - qual <17:
	print('você ainda não precisa se alistar!')
elif ano - qual > 17:
	print(f'você deveria ter se alistado {falta} anos atrás!')
elif ano - qual == 17:
	print('voce deve se alistar esse ano!')