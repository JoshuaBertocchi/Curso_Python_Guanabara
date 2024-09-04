salario=float(input('Me informe seu salário:'))

calculo10= ((salario*10)/100)
calculo15= ((salario*15)/100)
salario10= salario+calculo10
salario15= salario+calculo15


if salario > 1250:
    print(f'Você ganhou um aumento de 10%({calculo10:.2f}), seu salário atual será:R${salario10:.2f}')

else:
    print(f'Você ganhou um aumento de 15%({calculo15:.2f}), seu salário atual será:R${salario15:.2f}')