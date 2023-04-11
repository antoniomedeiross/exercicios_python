s=int(input('qual o seu salário em R$? '))
if s > 1250:
	a=(s/100)*110
else:
	a=(s/100)*115
print('o seu novo salário será: R$', a )