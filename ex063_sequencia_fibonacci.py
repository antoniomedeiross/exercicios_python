print('====SEQUÊNCIA FIBONACCI====')
n=int(input('qual o tamanho da sequência vc quer? '))

a=c=0
b=1
while c < n:
	print( b, end=' ')
	

	b_v=b
	b=a+b_v
	a=b_v
	
	c+=1