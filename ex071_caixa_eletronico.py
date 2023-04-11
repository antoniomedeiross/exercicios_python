print('==========CAIXA ELETRÔNICO==========')

valor=int(input('informe o valor que  deseja sacar: '))
a= valor//50*50
b=(valor-a)//20*20
c=(valor-a-b)//10*10
d=(valor-a-b-c)


print(f'''{'#'*50}
voce irá retirar:
{'#'*50}
{'='*50}
{a//50} notas de R$50
{'='*50}
{b//20} notas de R$20
{'='*50}
{c//10} notas de R$10
{'='*50}
{d} notas de R$1
{'='*50}''')