print('-='*9, 'Multiplos de 3, até 500', '=-'* 9)
for i in range(0, 500):

    calculo = i % 3

    if calculo == 0:
        print(f'N°:{i}')

print('Fim')