#EXERCÍCIO 7: LATAS DE TINTA

m = float(input('Quantidade de m² a serem pintados: '))

if m%54 == 0:
    latas = m/54
else:
    latas = int(m/54)+1

valor = latas * 80

print('Você precisa de %d latas de tinta.' %latas)
print('Valor a pagar de R$: %.2f.' %valor)
