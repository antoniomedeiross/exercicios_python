from math import factorial 
num= int(input('qual número vc deseja saber o fatorial? '))

fatorial= factorial(num)
f=num
print(f'o fatorial de {num} é: ')
while f > 0:
	print(f , end=' ') 
	print(' x ' if f >0 else ' = ', end=' ')
	f=f-1
print(fatorial)