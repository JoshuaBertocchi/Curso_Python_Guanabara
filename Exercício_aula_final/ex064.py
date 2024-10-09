continuar = True
cont = 0
somador = 0
while True: 
    n = int(input('Digite um número:  '))
    if n == 999:
        break
    cont += 1
    somador += n
print(f'''
      Quantidade de números: {cont} | {somador} 
''')
