tabela='palmeiras','internacional', 'fluminense','corinthians','flamengo', 'atlético-pr','atlético-mg','fortaleza','são paulo','américa-mg','botafogo','santos','goiás', 'bragantino','coritiba','cuiabá','ceará-sc','atlético-go','avaí','juventude'



print(f'''=====TABELA BRASILEIRÃO(2022)======
{'='*50}
os 5 primeiros colocados são:
{tabela[:5]}
{'='*50}
os 4 últimos colocados são:
{tabela[-4:]}
{'='*50}
lista em ordem alfabética:
{sorted(tabela)}
{'='*50}
posicão do flamengo:
{tabela.index('flamengo')+1}
''')