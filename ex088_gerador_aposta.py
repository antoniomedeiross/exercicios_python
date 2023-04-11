print('#'*30)
print('          MEGA SENA          ')
print('#'*30)
from time import sleep
from random import randint 
apostas=[]
v=int(input('quantas apostas vc deseja: '))
for a in range(0, v):
	na=[]
	for b in range (0,6):
		na.append(randint(0,61))
	apostas.append(na)
print ('-'*30)
print('suas apostas foram:')
print ('-'*30)
for c in range (0,v):

	print(f'jogo {c+1}: {apostas[c]}')
	sleep(2)