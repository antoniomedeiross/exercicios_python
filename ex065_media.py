res=''
n=0
media=0
cont=0
while True:
	n=int(input('dígite o número: '))
	res=input('quer contiuar? [S/N] ')
	cont+=1
	media+=n
	if res in 'nN':
		break
print(f'voce dígitou {cont} números, a média foi de  {media/cont}')