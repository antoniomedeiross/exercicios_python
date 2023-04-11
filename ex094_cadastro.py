d={}
l=[]
cont=0
lm=0
listaf=[]
media=0
listamedia=[]

while True:
	d['nome']=input('nome: ')
	d['sexo']=str(input('sexo [M/F/O]: ')).lower()
	d['idade']=int(input('idade: '))
	l.append(d.copy())
	cont+=1
	media+=d["idade"]


#verifica o sexo e coloca em uma lista se for 'f'
	if d["sexo"] == 'f':
		lm+=1
		listaf.append(d["nome"])
#controle de break
	stop=input('quer continuar? [S/N]').upper()
	if stop in 'Nn':
	 	break
	 	
	 	
media=media/cont

for a in l:
	if a["idade"] > media:
		listamedia.append(a)

print('#'*50)
z='='*50
print(f'foram cadastradas {cont} pessoas')
print(f'''{z}
as mulheres foram {lm}
{z}
lista de mulheres
 {listaf}
 {z}
 pessoas acima da média ({media})
 {listamedia}
 {'#'*50}''')
 