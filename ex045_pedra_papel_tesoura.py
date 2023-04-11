import random
print('escolha sua opcões \n [ 0 ] PEDRA \n [ 1 ] TESOURA \n [ 2 ] PAPEL ')
escolha=int(input())
comp=random.randint(0,3)
print(f'você escolheu {escolha}, o computador ecolheu {comp}')
if escolha == 0 and comp == 1 or escolha == 1 and comp == 2 or escolha == 2 and comp == 0:
	print('jogador venceu!')
elif escolha == comp:
	print('empate')
else:
	print('o computador venceu!')
	
	