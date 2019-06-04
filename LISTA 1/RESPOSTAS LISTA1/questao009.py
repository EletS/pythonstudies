#EXERCÍCIO 9: ALUGUEL

d = float(input('Quantidade de dias: '))
km = float(input('Quantidade de km rodados: '))

p = 60*d + 0.15*km

print('Valor a pagar: R$ %.2f' %p)
