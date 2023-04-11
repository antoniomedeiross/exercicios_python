from random import randint
from time import sleep
from operator import itemgetter
#cria uma biblioteca e uma lista 
jogadores={}
rank={}
#cria um laço que escolhe os valores das chaves do dicionário 
print('#'*40)

for a in range (1,5):
	jogadores[f'jogador{a}']=randint(1,6)

print('#'*40)
print ('JOGANDO OS DADOS...')
print('='*40)


#mostra os valores 

for k, v in jogadores.items():
	print(f'o {k} tirou = {v} ')
	sleep(1.5)
rank = sorted(jogadores.items() , key=itemgetter(1),reverse=True)	
#valores em ordem decrescente
print('#'*40)
print('ORDEM')
for k, v in rank:
	print(f'{k} tirou {v}')