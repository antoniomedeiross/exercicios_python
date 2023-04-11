lista=[]
while True:
	a=(int(input('informe o valor: ')))
	
	
	if a in lista:
		print('o valor ja foi informado, não sera adicionado novamente! ')
	else:
		lista.append(a)
	stop=input('quer continuar [S/N]:').upper()					
	if stop == 'N':
		break
print(sorted(lista))