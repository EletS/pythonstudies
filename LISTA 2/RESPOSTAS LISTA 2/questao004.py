#EXERCÍCIO 4: MAIOR

x1 = float(input('Número 1: '))
x2 = float(input('Número 2: '))
x3 = float(input('Número 3: '))

if x1 > x2 > x3 or x1 > x3 > x2:
    print(x1)
elif x2 > x1 > x3 or x2 > x3 > x1:
    print(x2)
else:
    print(x3)
