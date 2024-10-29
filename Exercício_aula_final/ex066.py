cont = soma = 0

while True:
    n= int(input('Digite um valor[999 para parar]: '))
    cont += 1
    if n == 999:
        break
    soma += n
print(f'Quantidade Digitados: {cont} Soma: {soma}')