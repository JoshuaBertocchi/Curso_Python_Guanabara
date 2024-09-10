from time import sleep
num = int(input('Digite um número:'))

valor = int(input(f'Converta o valor para:\n'
              f' 1- Para Binário\n'
              f' 2- Para Octal\n'
              f' 3- Para Hexadecimal\n Qual será o valor?'))
if valor == 1:
    print(f'Esse é o valor escolhido:{num}\nEsse é o valor convertido para Binário: {bin(num)[2:]}')
elif valor == 2:
    print(f'Esse é o número escolhido:{num}\nEsse é o número convertido para Octal: {oct(num)[2:]}')
elif valor == 3:
    print(f'Esse é o número escolhido:{num}\nEsse é o número convertido para Hexadecimal: {hex(num)[2:]}')

else:
    print('Algo deu errado, Tente novamente!')