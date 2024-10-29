
pri_termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = pri_termo
contador = 1
print(pri_termo, end=' =>')
while contador <= 10:
    contador += 1
    termo += pri_termo
    print(f' {termo}', end='')
    print( ' => ' if contador <= 10 else ': ', end='')
    
print('FIM')