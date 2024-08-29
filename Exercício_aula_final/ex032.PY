
print('='*30, 'ANO BISSEXTO!!!','='*30)

ano=int(input('Me informe o ano:'))

calculo_01= ano % 4
calculo_02= ano % 100
calculo_03= ano % 400
print(calculo_02)
if calculo_01 and  == 0:
    print('Estou pensando...')
if calculo_02 != 0 or calculo_03 == 0:
    print(f'{ano} É um ano Bissexto!!!')

else:
    print(f'{ano} Não é Bissexto.')



