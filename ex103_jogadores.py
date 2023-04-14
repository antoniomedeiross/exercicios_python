def ficha(j, g):
	if j == ' ' or j== '':
		j= '<DESCONHECIDO>'
	if g == ' 'or g== '':
		g = 0
	resultado = f'o jogadorª {j} fez {g}  gol(s) no campeonato! '
	return resultado
	
	
print(ficha(j=input('nome: '), g = input ('gols: ')))