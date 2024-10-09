from math import factorial

print('---CALCULE FATORIAL---')
n = int(input('Digite o valor: '))
n_fac = factorial(n)
contador = n + 1
print(f'{n}!',end='')
for i in range(n, 0,-1):
    print(f'{i}x', end= '')
print(f'={n_fac}')

while contador != 1:
    contador -= 1
    print(f'{contador}x', end='')
print(f'={n_fac}')