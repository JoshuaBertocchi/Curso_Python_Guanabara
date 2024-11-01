print('='*30)
print(f'{'|Somador de compras|':^30}')
print('='*30)
cont_produtos = soma_geral_produtos = cont_produtos_1000= 0
preco_mais_barato= 0
prod_mais_barato= ''
while True:
    cont_produtos += 1
    print(f'{'=| Dados do produto |=':^30}')

    nome_p = str(input('Nome:')).strip().upper()
    preco= (str(input('Valor: R$ '))).replace(',','.')

    try:
        preco = float(preco)
    except ValueError:
        print('Valor inválido! Por favor, insira um número válido.')
        break
    
    soma_geral_produtos += preco

    if preco >= 1000:
        cont_produtos_1000 += 1

    if cont_produtos == 1:  
        preco_mais_barato = preco
        prod_mais_barato = nome_p
    elif preco < preco_mais_barato:  
        preco_mais_barato = preco
        prod_mais_barato = nome_p

    per_continuar = str(input('Deseja continuar? [S ou N]')).upper().strip()
    if per_continuar ==  'S':
        continue
    else:
        break
print('='*30)
print(f'Total de Produtos:{cont_produtos}\nTotal Valor: R${soma_geral_produtos:.2f}\nProduto mais barato: {prod_mais_barato}, Valor: R${preco_mais_barato:.2f}')
print('='*30)