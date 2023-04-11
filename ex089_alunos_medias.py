lista=[]
nomeidade=[]
while True:
	nomeidade.append(input('nome: '))
	nomeidade.append(float(input('nota1: ')))
	nomeidade.append(float(input('nota2: ')))
	lista.append(nomeidade[:])
	nomeidade.clear()
	stop=input('quer continuar [S/N] ').upper()
	
	if stop in 'Nn':
		break
		
print('#'*40)
print('               MÉDIAS                 ')
print('#'*40)
print('Nº    NOME           ',end='')
print('MÉDIA')
print ('-'*40)

n=1

for c in lista:
	m=(c[1]+c[2])/2
	print(f'{n}     {c[0]:<15} {m}')
	print('-'*40)
	n+=1
	
while True:
	nota=int(input('qual aluno deseja saber as notas [(999) para encerrar]'))
	if nota == 999:
		break
	print(f'as notas de {lista[nota-1][0]} foram: {lista[nota-1][1]} e {lista[nota-1][2]}') 	
print('ENCERRADO!')