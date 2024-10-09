print('-='*8, '10 Primeiros termos da PA', '=-'*8)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(f'{c}', end=' => ')
print('FIM')