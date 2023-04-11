#analidor nomes
nome=input('digite seu nome: ')
print('maiusculo: ',nome.upper())
print('minusculo: ',nome.lower())
a1=nome.replace(" ", "")
print('letras sem espaços: ',len(a1))
a2= nome.split()
print('letras do 1º nome: ',len(a2[0]))