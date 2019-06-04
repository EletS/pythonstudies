#EXERCÍCIO 3: PEIXARIA

pesoPeixe = float(input('Quantidade de peixe em kg do dia: '))

excesso = pesoPeixe - 50
multa = excesso*4

if excesso > 0:
    print('Você excedeu %.1f kg, pague %.2f' %(excesso, multa))
else:
    excesso, multa = 0,0
    print('Você excedeu %.1f kg, pague R$ %.2f' %(excesso, multa))
