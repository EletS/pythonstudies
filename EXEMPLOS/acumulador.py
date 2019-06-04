#média de inteiros

x = 1
soma = 0

while x <= 10:
    y = int(input('%d numero: ' %x))
    soma = soma + y
    x = x+1
print('Média: %d' %(soma/10))
