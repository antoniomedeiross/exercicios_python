num='zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito', 'dezenove','vinte'

while True:
	a=int(input('dígite um número entre 0 e 20: '))
	if a >= 0 and a <= 20:
		break
	else:
		print('número inválido! tente novamente')
print(f'o número que vc dígitou foi {num[a]}')