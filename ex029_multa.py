v=int(input('qual a velocidade? '))
if v > 80:
	print('você foi MULTADO! ')
	m=(v-80)*7
	print(f'a sua multa será de R${m} ')
else:
	print('parábens, você respeita as leis de trânsito!')
	