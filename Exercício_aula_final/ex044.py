
from time import sleep

produto_valor = float(input('Informe o valor do produto. R$:'))
pay_options = float(input('''Opções de pagamento:
[1] Dinheiro/Cheque
[2] Cartão
[3] Pix
Digite o número da opção escolhida:'''))
#! 01-Calculo 10%
calculo_10 = produto_valor - ((produto_valor*10)/100)
#! 02-Calculo 5%
calculo_05 = produto_valor - ((produto_valor*5)/100)

if pay_options == 1 :
    print(f'Valor da sua compra:{produto_valor}\n'
          f'Opção de pagamento:Dinheiro/Cheque\n'
          f'Valor final com 10% de desconto. R$:{calculo_10}')
elif  pay_options == 3:
    print(f'Valor da sua compra:{produto_valor}\n'
          f'Opção de pagamento:Pix\n'
          f'Valor final com 10% de desconto. R$: {calculo_10}')
elif pay_options == 2:
    #! 03-Calculo 20%
    calculo_20 = produto_valor + ((produto_valor*20)/100)
    print('Opção de pagamento escolhida: Cartão')
    n_parcelas= int(input(f''' Escolha as opção abaixo:
    [1] À vista:{calculo_05:.2f}
    [2] 2x R$:{calculo_05/2:.2f}, Valor final: R${calculo_05:.2f}.
    [3] 3x R$:{(calculo_20 + (calculo_20*0.03))/3:.2f}, Valor final: R${calculo_20 + (calculo_20*0.03):.2f}.
    [4] 4x R$:{(calculo_20 + (calculo_20*0.04))/4:.2f}, Valor final: R${calculo_20 + (calculo_20*0.04):.2f}.
    [5] 5x R$:{(calculo_20 + (calculo_20*0.05))/5:.2f}, Valor final: R${calculo_20 + (calculo_20*0.05):.2f}.
    [6] 6x R$:{(calculo_20 + (calculo_20*0.06))/6:.2f}, Valor final: R${calculo_20 + (calculo_20*0.06):.2f}.
    [7] 7x R$:{(calculo_20 + (calculo_20*0.07))/7:.2f}, Valor final: R${calculo_20 + (calculo_20*0.07):.2f}.
    [8] 8x R$:{(calculo_20 + (calculo_20*0.08))/8:.2f}, Valor final: R${calculo_20 + (calculo_20*0.08):.2f}.
    [9] 9x R$:{(calculo_20 + (calculo_20*0.09))/9:.2f}, Valor final: R${calculo_20 + (calculo_20*0.09):.2f}.
    [10] 10x R$:{(calculo_20 + (calculo_20*0.1))/10:.2f}, Valor final: R${calculo_20 + (calculo_20*0.1):.2f}.
    [11] 11x R$:{(calculo_20 + (calculo_20*0.2))/11:.2f}, Valor final: R${calculo_20 + (calculo_20*0.2):.2f}.
    [12] 12x R$:{(calculo_20 + (calculo_20*0.25))/11:.2f}, Valor final: R${calculo_20 + (calculo_20*0.25):.2f}.
    Qual será o número de parcelas?'''))
    if n_parcelas >= 3 and n_parcelas <= 12:
        print(f'Ótimo, opção aceita! Em {n_parcelas}x.')
        print('Processando...')
        sleep(2)
        print('Pagamento Aceito!')
    elif n_parcelas == 2 or n_parcelas == 1:
        print(f'Ótimo, opção aceita! Em {n_parcelas}x.')
        print('Processando...')
        sleep(2)
        print('Pagamento Aceito!')
    else:
        print('Algo deu errado :/')


else:
    print('Algo deu errado')



