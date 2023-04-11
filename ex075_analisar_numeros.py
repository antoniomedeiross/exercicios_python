num=int(input('dígite um valor: ')),int(input('dígite um valor: ')),int(input('dígite um valor: ')),int(input('dígite um valor: '))


print(f'o 9 apareceu {num.count(9)} vezes')
if 3 in num:
	print(f'o número 3 apareceu na posicão {num.index(3)+1}')
else:
	print('o número 3 não apareceu')
print('os números pares foram',end=' ')
for n in num:
	if n % 2==0:
		print(n,end=' ')