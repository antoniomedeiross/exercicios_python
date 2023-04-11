preco= float(input('informe o preço do produto R$: '))
print('FORMAS DE PAGAMENTO \n (1) à vista(dinheiro/cheque) \n (2) à vista (cartão) \n (3) até 2× cartão \n (4) 3× ou mais no cartão')
forma=int(input('qual forma de pagamento deseja (1) (2) (3) ou (4)? '))

if forma == 1:
	valor= (preco/100)* 90
elif forma ==2:
	valor= (preco/100)*95
elif forma ==3:
	valor= preco
elif forma ==4:
	valor= (preco/100)*120
print(f'o valor final será R${valor}')