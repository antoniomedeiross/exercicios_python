n1=float(input('primeira nota: '))
n2=float(input('segunda nota: '))
media=(n1 + n2)/2
if media > 7:
	print(f'sua média foi de {media}, \033[42mvoce foi aprovado!\033[m] ')
elif media < 5:
	print(f'sua média foi de {media}, \033[41mvoce foi reprovado!\033[m')
else:
	print(f'sua média foi {media}, \033[43mvoce esta na recuperação!\033[m')