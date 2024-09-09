num_01=int(input('Me diga um número inteiro:'))
num_02=int(input('Me diga mais um número inteiro:'))

if num_01 > num_02:
    print(f'O primeiro valor é maior')
elif num_02 > num_01:
    print(f'O segundo valor é maior')
elif num_02 == num_01:
    print('Não existe valor maior, os dois são IGUAIS!')
else:
    print('Oxe! Deu algo errado.:/')