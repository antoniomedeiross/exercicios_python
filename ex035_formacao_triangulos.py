a=int(input('informe o maior lado do triângulo: '))
b=int(input('informe o 2º lado: '))
c=int(input('informe o 3º lado: '))

if a< b + c and b < a + c and c < a+b:
	print('o triângulo pode ser formado!')
else:
	print('o triângulo não pode ser formado!')
	