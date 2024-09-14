from datetime import  date
pessoas = int(input('Quantas pessoas serão analisadas?'))
contador=0
contador1=0
n=1
ano_atual= date.today().year
for i in range(1,pessoas+1):
    ano_pessoas = int(input(f'{i}. Me informe que ano você nasceu?'))
    idade= ano_atual - ano_pessoas

    if idade >= 21:
        contador += 1


    elif idade <= 20 and idade >= 20:
        n = contador1 + i
print(f'N°Pessoas maiores de idade:{contador}')
print(f'N°Pessoas menores de idade:{n}')