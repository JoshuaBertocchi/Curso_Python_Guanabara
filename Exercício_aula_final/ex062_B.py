
pri_termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
contador = 0
while True:
    contador += 1
    pa = pri_termo + (contador - 1) * razao
    print(f' {pa}', end='=>')
    if contador == 10:
        n = int(input('\nQuer ver mais quantos termos?\nSe não digite 0: '))
        if n != 0:
            contador += n
            continue
        elif n == 0:
            break
print('FIM')