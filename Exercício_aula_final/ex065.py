
n_menor = 0
n_maior = 0
cont = 0
somador = 0
while True:
    cont += 1 
    n = int(input('Digite um número: '))
    continuar_ou_n = str(input(''' 
    
    1 - Continuar Digitando
    2 - Encerrar Programa
   | O que deseja fazer? |
'''))
    somador += n
    media = somador / cont
    if cont == 1:
        n_menor = n
        n_maior = n
    if n > n_maior:
        n_maior = n
    if n < n_menor:
        n_menor = n
    elif continuar_ou_n == '2':
        print('Programa finalizado!')
        break
    elif continuar_ou_n == '1':
        continue
    else:
        print('Algo deu errado')
    

print(f' Média: {media}| Maior n°:{n_maior} | Menor n°:{n_menor}')