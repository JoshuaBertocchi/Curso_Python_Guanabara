

print('---CALCULE FATORIAL---')
n = int(input('Digite o valor: '))
f = 1 
contador = n
print(f'{n}!',end='')

while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end= ' ')
    f *= contador
    contador -= 1
print(f)