print('-=='*8, 'Calcule sua Média','==-'*8)
nota_01=float(input('Me informe sua 1° nota:'))
nota_02=float(input('Me informe sua 2° nota:'))
nota_03=float(input('Me informe sua 3° Nota:'))

calculo_media= (nota_01 + nota_02 + nota_03)/3

if calculo_media < 5.0:
    print(f'Média= {calculo_media:.2f}\n Situação: Reprovado')
elif (calculo_media > 5.0) and (calculo_media <= 6.9) or (calculo_media == 6.9):
    print(f'Média= {calculo_media:.2f}\n Situação: Recuperação')
elif calculo_media >= 7.0:
    print(f'Média={calculo_media:.2f}\n Parabéns, você foi Aprovado!')
