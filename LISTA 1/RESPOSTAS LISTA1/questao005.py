#EXERCÍCIO 5: DESCONTO

p = float(input('Valor do produto: '))
d = float(input('Porcentgem do desconto: '))

desconto = p*d/100
precofinal = p - desconto

print('Desconto de R$ %.2f' %desconto)
print('Valor final do produto: R$ %.2f' %precofinal)
