salário=float(input('Me informe seu salário:'))
if salário <= 1250:
    novo = salário + (salário * 15 /100)
else:
    novo = salário + (salário * 10 /100)

print(f'Quem ganhava R$ {salário:.2f} passa a ganhar R${novo} agora.')