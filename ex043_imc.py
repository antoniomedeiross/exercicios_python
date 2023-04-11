kg= float(input('informe seu peso em kg: '))
alt=float(input('informe sua altura em metros: '))
imc=kg/alt**2

if imc < 18.5:
	massa=('\033[41m abaixo do peso \033[m')
elif imc <= 25:
	massa=('\033[42m peso ideal \033[m')
elif imc <= 30:
	massa=('\033[44m sobrepeso \033[m')
elif imc <= 40:
	massa=('\033[45m obesidade \033[m')
elif imc > 40:
	massa= ('\033[41m obesidade morbida \033[m')
print(f'o seu imc é {imc}, considerado {massa}')