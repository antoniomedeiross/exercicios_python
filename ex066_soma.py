s = n = q = 0
while True:
	n=int(input('dígite um número: ([999] para parar) '))
	if n == 999:
		break
	s += n
	q += 1
print(f'foram dígitados {q} números e a soma deles foi {s}!')