def leiaint(x):
		try:
			int(x)
		
		except:
			while not x.isnumeric():
				
				print('\033[1;31m NÚMERO INVÁLIDO!\033[m')
				x = input('tente novamente: ')
		finally:
			return x			
	
	

def leiafloat(x):
    while not isinstance(x, (float)):
        try:
            x = float(x)
        except:
            print('\033[1;31m NÚMERO INVÁLIDO!\033[m')
            x = input('tente novamente: ')
    return x
    
	
	
inteiro=leiaint(input('informe um número inteiro: '))
real=leiafloat(input('informe um real: '))
	
	
	
	
print(f'voce digitou o inteiro {inteiro}, e o real {real}')