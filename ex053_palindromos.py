frase=input('dígite uma frase:')
normal=frase.upper().replace(' ', '')
contrario=frase.upper().replace(' ','') [ : : -1]
if normal == contrario:
	print(f'{normal} ao contrario é {contrario} \nÉ UM PALÍNDROMO')
else:
	print(f'{normal} NÃO É UM PALÍNDROMO')