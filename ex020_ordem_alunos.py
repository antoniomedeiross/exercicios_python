import random
a1=input('aluno1: ')
a2= input('aluno2: ')
a3= input('aluno3: ')
lista= [a1, a2 , a3] 
random.shuffle(lista)
print('a ordem será:')
for a in lista:
	print(a)