#Leitura de consoante

array = []
i = 0
soma = 0
while i < 10:
    a = input('Letra: ')
    array.append(a)
    if a not in 'aeiou':
        soma += 1
    i+=1
print(soma, 'consoantes')
