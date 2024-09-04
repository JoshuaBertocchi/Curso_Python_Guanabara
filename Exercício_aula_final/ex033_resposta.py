a=int(input('Digite o 1° número:'))
b=int(input('Digite o 2° número:'))
c=int(input('Digite o 3° número:'))
# Verificando o menor valor
menor = a
if b < a and b < c:
      menor = b
if c < a and c < b:
      menor = c
# Verificando o maior valor
maior = a
if b > a and b > c:
      maior = b
if c > a and c > b:
      maior = c
print(f'O maior número é:{maior}.'
      f'\nO menor número é:{menor}.')

