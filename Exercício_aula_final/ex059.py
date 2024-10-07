
valor_1 = int(input('Me informe um valor: '))
valor_2 = int(input('Me informe outro valor: '))

while True:

    res = ''
    print('''---|Escolha o que será feito|---
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')

    valor = int(input('Qual será a opção? '))

    if valor == 1:
        soma = valor_1 + valor_2
        print(f'A soma do valor {valor_1} e o valor {valor_2} é igual a {soma}.')

    elif valor == 2:
        multiplicacao = valor_1 * valor_2
        print(f'A multiplicação dos valores {valor_1} e {valor_2} é igual a {multiplicacao}.')
    elif valor == 3:
        if valor_1 > valor_2:
            print(f'O maior valor é {valor_1}.')
        else:
            print(f'O maior valor é {valor_2}.')
    elif valor == 4:
        valor_1 = int(input('Me informe um valor: '))
        valor_2 = int(input('Me informe outro valor: '))
    elif valor == 5:
        print('Sair do programa.')
        break
    else:
        print('Opção invalida, tente novamente.')
print('Programa finalizado.')
