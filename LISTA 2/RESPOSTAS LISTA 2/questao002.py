#EXERCÍCIO 2: ANO BISSEXTO

ano = int(input('Ano: '))

if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('Ano bissexto')
else:
    print('Ano não é bissexto')
    
