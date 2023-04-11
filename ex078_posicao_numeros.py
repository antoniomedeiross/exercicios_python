lista=[int(input('dígite o número: ' )), int(input('dígite o número: ' )), int(input('dígite o número: ' )),int(input('dígite o número: ' )),int(input('dígite o número: ' ))]

a=max(lista)
b=min(lista)

maximo=[]
minimo=[]

for c in range(0,5):
	if lista[c] == a:
		maximo.append(c)
	if lista[c] == b :
		minimo.append(c)
		
	
print(f'''o maior número foi: {a} na posição {maximo}
o menor foi {b} na posição {minimo}''' )
