total18 = totalH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M|F] ')).strip().upper()[0]
    if idade <= 18:
        total18 += 1
    if sexo == 'M':
        totalH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S|N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total Pessoas maiores de 18 {total18}')
print(f'Ao todo temos {totalH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos.')