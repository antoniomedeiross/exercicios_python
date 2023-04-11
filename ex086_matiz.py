matriz= [[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0]]
print('digite os números que irão fazer parte da matriz')
for l in range (0, 3):
	for c in range (0, 3):
		matriz[l][c]=int(input('dígite o número: '))
for l in range(0, 3):
	for c in range (0, 3):
		print(f'[{matriz[l][c]}]',end='')
	print()