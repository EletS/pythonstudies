#EXERCÍCIO 6: SALÁRIO

hora = float(input('Quantidade de horas trabalhadas: '))
valor = float(input('Valor das horas trabalhadas: '))

bruto = hora*valor
ir = bruto*0.11
inss = bruto*0.08
sind = bruto*0.05

liq = bruto - ir - inss - sind

print('+ Salário Bruto: R$ %.2f' %bruto)
print('- IR: R$ %.2f' %ir)
print('- INSS: R$ %.2f' %inss)
print('- Sindicato: R$ %.2f' %sind)
print('= Salário Líquido: R$ %.2f' %liq)
