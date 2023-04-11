menor=maior=0

for c in range(0, 5):
	x=float(input(f'dígite o peso da {c+1}ªpessoa: '))
	if x > maior:
		maior=x
	if c == 1:
		menor=x
	if menor > x:
		menor=x

print(f'o menor peso informado foi {menor}, e o maior foi {maior}')
