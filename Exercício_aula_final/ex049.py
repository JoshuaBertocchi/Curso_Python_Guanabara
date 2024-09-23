from time import sleep
n_1 = int(input('Me diga um número: '))
n_2 = int(input('Até que número você quer saber a tabuada?'))
print('Calculando a tabuada!!!')
sleep(1)
for i in range(1, n_2+1):
    calculo= n_1 * i
    sleep(0.1)
    print(f'{n_1} X {i} = {calculo}')

print(f'Essa é a tabuada de {n_1} até {n_2}.')


