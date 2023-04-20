import webbrowser

try:
	webbrowser.open("http://pudim.com.br/")
	
	
	
except:
	print('\033[31m não consegui acessar o site do pudim ;( \033[m')

else:
	print('\033[32mo site do pudim está acessível ;) \033[m')