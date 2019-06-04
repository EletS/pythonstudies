#exercíio empresa de telefonia

minuto = float(input('Minutos usados: '))

if minuto < 200:
   preço = 0.20
elif minuto <= 400:
    preço = 0.18
elif minuto <= 800:
    preço = 0.15
else:
    preço = 0.08
            
print('Conta: R$ %.2f.' %(minuto*preço))
    
