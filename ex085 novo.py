lista=[[],[]]
valor=0
for c in range (1,8):
	valor=int(input(f'dígite o {c}° valor: '))
	if valor % 2 == 0:
		lista[0].append(valor)

			
			
	else:
		lista[1].append(valor) 
	valor=0

lista[0].sort()
lista[1].sort()
print(f'''os números pares foram: {lista[0]}
os ímpares foram {lista[1]}''')