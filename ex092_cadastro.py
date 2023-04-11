from datetime import datetime
d={}
d['nome']=input('nome: ')
idade= int(input('ano de nascimento: '))
d['idade']= datetime.now().year  - idade
ct=int(input('carteira de trabalho, (0 se não tiver): '))


if ct != 0:
	d['ct']=ct
	d['contratação']=int(input('ano de contratação: '))
	d['salario']=int(input('salario: '))
	print('#'*40)
	print(f'''nome tem valor {d["nome"]}
Idade tem valor {d["idade"]}
ct tem valor {d["ct"]}
contratação tem valor {d["contratação"]}
salário tem valor {d["salario"]} 
aposentadoria tem valor {d["contratação"]+35-idade}''')
else:
	d['ct']=0
	print('#'*40)
	print(f'''nome tem valor {d["nome"]}
Idade tem valor {d["idade"]}
ct tem valor {d["ct"]} ''')