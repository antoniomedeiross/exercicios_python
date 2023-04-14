def nota(*x, sit=False):
	"""
	função para analisar notas de vários alunos
	para sit: True retorna a situação do aluno 
	para x: nota do(s) alunos
	para dias: dicionário onde as informações ficam armazenadas 
	"""
	diss={}
	diss["total"] = len(x)
	diss["maior"] = max(x)
	diss["menor"] = min(x)
	diss["media"] = sum(x) / len(x)
	if sit == True:
		if 5 <= diss["media"] < 7:
			diss["sit"] = 'RAZOAVEL'  
		elif diss["media"] < 5:
			diss["sit"] = 'RUIM'
		else:
			diss["sit"] = 'BOA'
	print( diss)
nota(4,7,48,9,68, sit=True)

help(nota )