#EXERCÍCIO 10: CIGARRO

c = float(input('Qantidade de cigarros por dia: '))
a = float(input('Quantidade de anos fumando: '))

d = ((a * 365 * c) / 144)

print('Você já perdeu aproximadamente %.2f dias de vida' %d)
