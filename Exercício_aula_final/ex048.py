print('-='*9, 'Multiplos de 3, até 500', '=-'* 9)
cont = 0
soma = 0
for i in range(1, 501, 2):

    calculo = i % 3

    if calculo == 0:
        print(f'N°:{i}')
        cont = cont + 1
        soma = soma + i
print(f'Soma de todos os {cont} valores é {soma}.')