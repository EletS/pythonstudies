#LISTAS

nota = [4, 5, 6, 1, 6]
cont = 0
soma = 0

while cont <= 4:
    soma += nota[cont]
    cont += 1

print('Média = %.1f' %(soma/cont))
