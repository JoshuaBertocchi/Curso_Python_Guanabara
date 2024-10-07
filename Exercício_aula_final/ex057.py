
sexo = str(input('Me diga seu sexo [M ou F]:  ')).upper()

if sexo == 'M' or sexo == 'F':
    if sexo == 'M':
        print(f'Seu sexo é {sexo}. Masculino.')
    elif sexo == 'F':
        print(f'Seu sexo é {sexo}, Feminino.')

while sexo != 'M' and sexo != 'F':
    print(f'DIGITE APENAS M ou F!!!')
    sexo = str(input('Me diga seu sexo [M ou F]: ')).upper()
    if sexo == 'M' or sexo == 'F':
        if sexo == 'M':
            print(f'Seu sexo é {sexo}. Masculino.')
        elif sexo == 'F':
            print(f'Seu sexo é {sexo}, Feminino.')