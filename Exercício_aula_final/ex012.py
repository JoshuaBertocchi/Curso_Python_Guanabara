try:
    n1=float(input('Você ganhou 5% de desconto. Me diga o valor da sua compra:'))
    desconto01=n1*5/100
    desconto02=n1-desconto01
    print(f'Você ganhou R${desconto01:.2f} de desconto!!! Seu valor final ficou R${desconto02:.2f}')
except:
    print('Apenas VALORES BURRO!!!')