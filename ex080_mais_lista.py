lista = []

for c in range(1, 6):
    a = int(input(f'Digite o {c}º valor: '))

    if c == 1:
        lista.append(a)
    else:
        for i in range(len(lista)):
            if a <= lista[i]:
                lista.insert(i, a)
                break
        else:
            lista.append(a)

print(lista)
