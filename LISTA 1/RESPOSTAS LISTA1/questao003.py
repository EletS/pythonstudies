#EXERCÍCIO 3: SEGUNDOS
d = int(input('Insira a quantidade de dias: '))
h = int(input('Insira a quantidade de horas: '))
m = int(input('Insira a quantidade de minutos: '))
s = int(input('Insira a quantidade de segundos: '))

total = d * 86400 + h * 3600 + m * 60 + s
print ('O total em segundos é:', total)
