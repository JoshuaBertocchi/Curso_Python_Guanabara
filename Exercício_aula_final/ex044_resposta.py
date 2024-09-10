print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Valor da compra. R$:'))
print('''Formas de Pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
    print(f'Sua compra será no Dinheiro/Cheque com o valor final de R${total:.2f}. SEM JUROS')
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print(f'Sua compra será no Cartão à vista com o valor final de R${total:.2f}. SEM JUROS')
elif opção == 3:
    print(f'Sua compra será em 2x no cartão. Valor final R$:{preço:.2f}. SEM JUROS')
elif opção == 4:
    n_parcelas = int(input('Qual será o número de parcelas?'))
    total= preço + (preço * 20/100)
    print(f' Sua compra de R$ {preço:.2f} vai custar R$:{total:.2f} no final.')
    print(f' Sua compra será parcelada em {n_parcelas}x de {total/n_parcelas:.2f}, COM JUROS.')
else:
    print('Opção inválida de pagamento. Tente novamente!')