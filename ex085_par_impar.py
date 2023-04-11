lista=[]
impar=[]
par=[]
for c in range (1,8):
	n=int(input(f'dígite o {c}° valor: '))
	if n % 2 == 0:
		par.append(n)

			
			
	else:
		impar.append(n) 
	n=0
par.sort()
impar.sort()
lista.append(par[:])
lista.append(impar[:])
print(f'''os números pares foram: {lista[0]}
os ímpares foram {lista[1]}''')