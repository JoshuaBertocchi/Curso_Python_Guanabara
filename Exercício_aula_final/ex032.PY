
print('='*30, 'ANO BISSEXTO!!!','='*30)

ano=int(input('Me informe o ano:'))

calculo_01= ano % 4
calculo_02= ano % 100
calculo_03= ano % 400

if (calculo_01 == 0) and (calculo_02 != 0) or (calculo_03 == 0):
    print(f'{ano} É um ano Bissexto!!!')

else:
    print(f'O ano {ano} Não é Bissexto.')



