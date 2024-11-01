print('='*40)
print(f'{' Valor a sacar! ':^40}')
print('='*40)

nota_50 = 50
nota_20 = 20
nota_10 = 10
nota_01 = 1

valor = int(input('Valor: '))

div_50 = valor // nota_50
resto_50 = valor  % nota_50

div_20 = resto_50 // nota_20
resto_20 = resto_50  % nota_20

div_10 = resto_20 // nota_10
resto_10= resto_20 % nota_10

div_1 = resto_10 // nota_01
resto_1 = resto_10 % nota_01

print(div_10, resto_10)
print(f'Total de {div_50} de R$ 50\nTotal de {div_20} de R$ 20\nTotal de {div_10} de R$ 10\nTotal de {div_1} de R$ 1')
