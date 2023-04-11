#cria a variável dicionário e seus valores

aluno={}
aluno['aluno'] = str(input('nome do aluno: '))
aluno['media'] = float(input('média: '))
print(f'o aluno é {aluno["aluno"]}')
print (f'a média é {aluno["media"]}')

#printa a situação de aprovado ou reprovado 
if aluno["media"] < 5:
	print ('situação: aluno reprovado ')
else:
	print('situação: aluno aprovado ')