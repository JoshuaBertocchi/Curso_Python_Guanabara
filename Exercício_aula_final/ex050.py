cont = 0
soma_pares = 0 #* 01-Variável para acumular a soma dos números pares.
for i in range(1,6+1):
    valor_n = int(input(f'{i}. Me diga um número:'))
    par = valor_n % 2 #* 02- Verificar se o número é par.
    if par == 0:
        cont = i + 0
        soma_pares += valor_n #* 03- Faz a soma.


print(f'Você informou {cont} números pares e a soma foi: {soma_pares}')


