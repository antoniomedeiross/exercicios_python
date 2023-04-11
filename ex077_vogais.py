lista='amarelo','azul','blackpink', 'mamacita'

print(lista )
for p in lista:
	print(f'\nna palavra {p.upper()} as vogais são: ', end=' ')
	for l in p:
		if l.lower() in 'aãàâeéèêíìioóõôuú':
			print( l,end='')
	