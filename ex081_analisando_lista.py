lista=[]
cont=0
while True:
	a=int(input('dígite o valor: '))
	s=input('quer continuar [S/N]? ').upper()

	cont+=1
	lista.append(a)
			
				
	if s == 'N':
		break
	if 5 in lista:
		parte='5 faz parte da lista!'
	else:
		parte='5 não faz parte da lista'

print(f'''{'×'*40}
foram dígitados {cont} números.
a lista em ordem decrescente é: {sorted(lista,reverse=True)}
{parte}
{'×'*40}''')
	
	
	
