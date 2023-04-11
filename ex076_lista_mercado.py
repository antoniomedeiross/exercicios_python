lista='arroz','4,00', 'feijao','6,00','macarrao','1,50'
for c in range (0,len(lista)):
	if c % 2 == 0:
		print(f' {lista[c]:.<30}', end='')
	if c % 2 == 1:
		print(f'R$ {lista[c]:>6}')
