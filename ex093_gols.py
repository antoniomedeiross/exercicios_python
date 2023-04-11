d={}
gols=[]
total=0
d['nome']=input('nome do jogador: ')
p=int(input('quantas partidas jogadas: '))

for a in range (0,p):
	g=int(input(f'quantos gols no jogo {a}: '))
	gols.append(g)
	total+=g

d['gols']=gols
d['total']=total
print('#'*40)
print(d)
print(f'o jogador {d["nome"]} jogou {p} partidas')
for a in range (0,p):
	print(f'no jogo {a} ele fez {gols[a]} gols')