from random import randint
a=randint(1,10)

print('O COMPUTADOR VAI PENSAR EM UM NÚMERO DE 1 A 10, TENTE ADIVINHAR!')
b=int(input('qual o seu palpite? '))
t=0
while a != b:
	b=int(input('qual o seu palpite?' ))	
	t= t + 1
print(f'PARÁBENS VC VENCEU!\nDepois de {t} tentativas')