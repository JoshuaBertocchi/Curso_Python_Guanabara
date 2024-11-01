
cont_m = cont_f = menor18 = f_menor20 = 0 

print('='*25)
print(f'|{'CADASTRE UMA PESSOA':^23}|')
print('='*25)
while True:
    
    try: 
        idade = int(input('IDADE: '))
        while type(idade) != int:
            idade = int(input('IDADE: '))
        if idade > 120 or idade < 0:
            print(f'Digite sua idade REAL! Idade {idade} não existe!!!')
            continue
        sexo = str(input('Sexo:[M ou F] ')).strip().upper()
        while (sexo != 'M') and (sexo != 'F'):
            sexo = str(input('Me informe seu sexo:[M ou F] ')).strip().upper()
            print('Digite apenas M ou F!')
        if idade <= 18:
            menor18 += 1
        if sexo == 'M':
            cont_m += 1
        if sexo == 'F':
            if idade <= 20:
                f_menor20 += 1
        print('='*30)
        perg = str(input('Quer continuar? [S ou N] ')).strip().upper()

        if perg == 'S':
            continue
        else:
            break
    except:
        print('='*30)
        print('Informe apenas números inteiros!')  
        print('='*30)
        continue   
print(f'Quantidade de pessoas abaixo de 18: {menor18}\nQuantidade de homens: {cont_m}\nQuantidade de mulheres abaixo de 20:{f_menor20}')