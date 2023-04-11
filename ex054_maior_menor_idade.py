from datetime import date

ano=date.today().year
maior=0
menor=0
for c in range (1, 8):
	nas=int(input(f'qual o ano de nascimento da {c}ª pessoa: '))
	idade=ano-nas
	if idade >=18:
		maior += 1
	else: 
		menor += 1
print(f'dentre as pessoas {maior} sao maiores. e {menor} sao menores de idade!')
