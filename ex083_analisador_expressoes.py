exp=input('dígite uma expressão matemática: ')
list=[]
for n in exp:
  if n == '(':
    list.append(n)
  elif n == ')':
    if len (list)>0:
      list.pop()
    else:
      list.append(')')
      break
if len(list) == 0:
  print('sua expressão está correta! ')
else:
  print('sua expressão esta errada!')