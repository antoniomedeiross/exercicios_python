print('CADASTRO DE PESOAS')
a=b=c=d=0
while True:
	s=input('sexo: [M/F/OUTRO]').upper()
	idd=int(input('idade: '))
	if idd >= 18:
		a += 1
	if s == 'M':
		b+=1
	if s == 'F' and idd >= 20:
		c+=1
	if s == 'OUTRO':
		d+=1
	stop=input('quer continuar [S/N]? ').upper()
	if stop == 'N':
		break
print(f'voce cadastrou {a} pessoas maiores de 18 anos, {b} pessoas do sexo masculino e {c} mulheres com mais de 20 anos e {d} pessoas com sexo diferenfente de M e F!')