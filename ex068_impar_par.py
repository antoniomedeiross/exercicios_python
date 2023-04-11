from random import randint
n='a'
jog='a'
comp='b'
cont=0

while True:
	jog=input('impar ou par?')
	if jog == 'impar':
		comp='par'
	elif jog == 'par':
		comp='impar'
	n=int(input('qual número de 0 a 10 vc quer? '))
	c=randint(0,10)
	
	if jog == 'par' and (n+c)%2==0:
		print(f'voce jogou {n} e o computador jogou {c}, deu par, o jogador VENCEU!')
		break
	elif jog == 'impar' and (n+c)%2==1:
		print(f'voce jogou {n} e o computador jogou {c}, deu impar, o jogador VENCEU')
		break
	else:
		print('a máquina VENCEU')
		cont+=1
print('voce perdeu ', cont, ' vezes') 
		
	
