lista=[]
temp=[]
max=[]
min=[]

while True:
	temp.append(str(input('nome: ')))
	temp.append(float(input('peso: ')))
	
	if len(lista)==0:
		max=min=temp[1]
	else:
		if temp[1] > max:
			max=temp[1]
		if temp[1] < min:
			min=temp[1]
		
	lista.append(temp[:])
		
		
	temp.clear()
	
	
	stop=input('quer continuar [S/N]')
	if stop in 'nN':
		break
print('#'*40)
print(f'foram cadastradas {len(lista)} pessoas!')
print(f'o maior peso foi {max}kg de ', end='')
for n in lista:
	if n[1] == max:
		print(f' [{n[0]}]',end='')
print()
print(f'o menor peso foi {min}kg de ', end='')
for n in lista:
	if n[1] == min:
		print(f' [{n[0]}] ', end='')
