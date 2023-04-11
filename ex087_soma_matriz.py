par=0
matriz= [[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0]]
for l in range (0, 3):
	for c in range (0, 3):
		matriz[l][c]=int(input('dígite o número: '))
		if matriz[l][c] % 2 == 0:
			par+=matriz[l][c]
for l in range(0, 3):
	for c in range (0, 3):
		print(f'[{matriz[l][c]}]',end='')
	print()
print('#'*40)
print(f'a soma dos números pares é {par}')
print (f'a soma da terceira coluna é {matriz[2][0]+matriz[2][1]+matriz[2][2]}')
print(f'o maior valor da segunda linha é {max(matriz[1])}')