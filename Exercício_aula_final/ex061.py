
pri_termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
contador = 1
print(pri_termo, end=' =>')
while contador != 10:
    contador += 1
    pa = pri_termo + (contador - 1) * razao
    print(f' {pa}', end='=>')
print('FIM')