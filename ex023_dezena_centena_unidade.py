num=int(input('dígite um número: '))
m = num//1000
c = (num - (m)*1000)//100
d = (num- (m*1000+c*100))//10
u= num -((m*1000)+(c*100)+(d*10))

print('milhar: ' , m)
print('centena: ' , c) 
print('dezena: ' , d)
print('unidade: ' , u)