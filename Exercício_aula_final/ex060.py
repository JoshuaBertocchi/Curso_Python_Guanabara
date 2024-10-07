from math import factorial

print('---CALCULE FATORIAL---')
n = int(input('Digite o valor: '))
n_fac = factorial(n)

for i in range(n, 0,-1):
    print(f' {i}x', end= ' ')
print(f':{n_fac}')