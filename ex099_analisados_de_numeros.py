from time import sleep 
def maior(*n):
	print('analisando os valores passados...')
	print('#'*40)
	sleep(1)
	print(f'foram informados {len(n)} valores \nsão eles:')
	for a in (n):
		 print(a , end=' ', flush = True )
		 sleep(1)
	print()
	print(f'o maior dente eles é {max(n)}')


maior(1,4,7,9,4,9,5)