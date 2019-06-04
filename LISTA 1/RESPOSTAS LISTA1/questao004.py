#EXERCÍCIO 4: SALÁRIO
salario = float(input('Salário base: '))
aumento = float(input('Porcentagem de aumento: '))

aumento = salario * aumento / 100
salariofinal = aumento + salario
print('Aumento: R$ %.2f' %aumento)
print('Salário ajustado: R$ %.2f' %salariofinal)
