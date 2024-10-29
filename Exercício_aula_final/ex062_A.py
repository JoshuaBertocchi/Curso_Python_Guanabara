
pri_termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = pri_termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        contador += 1
        termo += pri_termo
        print(f' {termo} =>', end='')
    print(' PAUSA ')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print(f'Progressão finalizada com {total} termos mostrados.')    
print('FIM')