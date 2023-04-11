lista=[]
i=[]
p=[]
while True:
  a=int(input('dígite o número: '))
  lista.append(a)
  if a % 2 == 0:
    p.append(a)
  else:
    i.append(a)
  b=input('quer continuar [S/N]? ').upper()
  if b == 'N':
    break
print(f'''a lista dígitada foi {lista}
os números pares foram {p}
os números ímpares foram {i}''')