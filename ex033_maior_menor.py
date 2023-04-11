n1=int(input('dígite um número: '))
n2= int( input('dígite outro número: '))
n3=int(input('dígite outro número: '))
#descobrir maior
if n1 > n2 and n1> n3:
	maior=n1
if n2>n1  and n2>n3:
	maior=n2
if n3>n1 and n3>n1:
	maior=n3
#decobrir menor
if n1<n2 and n1<n3:
	menor=n1
if n2<n1 and n2<n3:
	menor=n2
if n3< n1 and n3<n2:
	menor=n3
	
print(f'o maior número é {maior}\no menor número é {menor}')
