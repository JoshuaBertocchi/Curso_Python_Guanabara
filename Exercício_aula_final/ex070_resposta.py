total= tot1000 =  menor = cont = 0
nome_menor = ' '
while True: 
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    resp = ' '
    if cont == 1:
        nome_menor = produto
        menor = preco
    else: 
        if preco < menor:
            nome_menor = produto
            menor = preco
    if preco >= 1000:
        tot1000 += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    
print(f'{'|FIM DO PROGRAMA|':-^40}')
print(f'Valor Total:"{total:.2f}')
print(f'Produtos acima de R$ 1000:{tot1000}')
print(f'O produto {nome_menor} é o mais barato e custa R$ {menor:.2f}')