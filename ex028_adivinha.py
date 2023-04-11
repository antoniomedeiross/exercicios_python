import random
n=(random.randint(1,5))
esc=int(input('escolha um número de 1 a 5: '))
if esc==n:
	print(f'o numero escolhido pelo computador foi {n}\nPARÁBENS!!! VOCÊ VENCEU!!!')
else:
	print(f'o numero escolhido pelo computador foi {n} \nvocê perdeu')	
