#Media de 4 notas

notas = []
i = 0
soma = 0

while i <= 3:
    soma = float(input('Nota: '))
    notas.append(soma)
    soma += notas[i]
    i += 1

print ('Notas:', notas)
print ('Média: %.1f' %(soma/i))
