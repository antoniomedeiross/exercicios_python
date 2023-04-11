print('=' * 5,'MERCADO','=' *5)

total=0
menor=0
mil=0
cont=0
barato=''
while True:
	nome=input('nome do produto: ')
	preco=float(input('preço: '))
	total+=preco
	cont+=1
	if cont == 1:
		menor+=preco
		barato=nome
	if preco >= 1000:
		mil+=1

	if preco <= menor:
		menor=preco
		barato=nome
	stop=input('quer continuar S/N? ').upper()
	
	
	
	
	if stop == 'N':
		break
print('='*50,f'''
a sua compra foi de {total}
{'='*50}
{mil} produtos custam mais de R$1000
{'='*50}
o produto mais barato foi {barato} por R${menor}
{'='*50}
FIM DAS COMPRAS
{'='*50}''')