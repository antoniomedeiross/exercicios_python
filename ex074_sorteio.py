from random import randint
from time import sleep

num=randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)
print('sorteanfo 5 número de 0 a 10...')
sleep(2)
for n in num:
	print(n)
print(f'o menor valor foi {min(num)}, e o maior foi {max(num)}')