lista=[]
maior=[]
menor=[]
while True:
	np = input('nome: '), int(input('peso: '))
	
  
	lista.append(np)
      
	if len(lista)==1:
		menor.append(np)
		maior.append(np)
	else:
		if np[1] > maior[0][1]:
			maior.pop(0)
			maior.append(np)

		if np[1] <  menor[0][1]:
			menor.pop(0)
			menor.append(np)
	stop=input('quer continuar [S/N]? ').upper()
	if stop == 'N':
  	  break


print(f'o menor peso foi de {menor[0][1]} = {menor[0][0]}  o maior foi {maior[0][1]} = {maior[0][0]}')