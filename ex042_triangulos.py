l1=int(input('informe os lados do triâgulos: '))
l2=int(input('informe os lados do triâgulo: '))
l3=int(input('informe os lados do triâgulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 :
	print('o triângulo é possivel')
else:
	print('o triângulo não é possivel!')
if l1==l2 and l2==l3:
	print('triangulo equilátero!')
elif l1==l2 or l2==l3 or l1==l3:
	print('triângulo isoceles')
elif l1 != l2 != l3 != l1:
	print('tiângulo escáleno')