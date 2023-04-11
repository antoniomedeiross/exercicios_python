ano= int(input('dígite o ano desejado: '))
if ano%4==0 and ano%100 !=0 or ano%400==0:
	print(f'o ano de {ano} é BISSEXTO! ')
else: print(f'o ano {ano} NÃO É BISSEXTO! ')
