d={}
gols=[]
total=0
j={}


while True:
	d['nome']=input('nome do jogador: ')
	p=int(input('quantas partidas jogadas: '))
	
	for a in range (0,p):
		g=int(input(f'quantos gols no jogo {a}: '))
		gols.append(g)
		total+=g
	
	d['gols']=gols
	d['total']=total
	
	
	j[d['nome']]=total	
	
	
	
	print('#'*40)
	print(d)
	print(f'o jogador {d["nome"]} jogou {p} partidas')
	for a in range (0,p):
		print(f'no jogo {a} ele fez {gols[a]} gols')
	print('#'*40)
	

	d.clear()
	gols.clear()
	total=0
	stop=input('quer continuar [S/N]').upper()
	if stop in 'nN':
		break
print ('=-'*30)		
print('jogador                 gols')	
print ('=-'*30)
for k, v in j.items():
	print(f'{k:.<25}{v}')
