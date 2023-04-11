print('TERMOS DE PROGRESSAO ARITIMETICA')
ti=int(input('termo inicial: '))
r=int(input('razão: '))
tf=10*r
print('os 10 primeiros teremos da progressão são:')
for c in range(ti , tf, r):
	print(c)