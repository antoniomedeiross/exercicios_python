casa=float(input('qual o valor da casa? '))
par=int(input('em quantas parcelas vc deseja pagar? '))
sal=float(input('qual o seu salário? '))
#decobrir o valor da parcela
ideal=casa/par
#porcentagem
porcentagem=(sal/100)*30
if ideal < porcentagem:
	print(f'o valor da parcela será de R${ideal:.2f}\n\033[42m o emprestimo foi aceito! \033[m')
elif ideal > porcentagem:
	print(f'o valor da parcela será de R${ideal:.2f}\n \033[41m o emprestimo NÃO foi aceito! \033[m' )