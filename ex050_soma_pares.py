soma=cont=0
for c in range (0, 6):
	valor=int(input(f'dígite o {c+1}° valor desejado: '))
	if valor % 2 == 0:
		cont+=1
		soma=soma+valor
print(f'voce informou {cont} númetos pares, a soma deles foi {soma}')