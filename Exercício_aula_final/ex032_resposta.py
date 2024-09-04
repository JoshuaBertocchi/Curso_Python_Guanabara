
from datetime import date #01-Usado para chamar o Parâmetro que identifica a data do pc que está rodando o código!
print('='*30, 'ANO BISSEXTO!!!','='*30)

ano=int(input('Me informe o ano:'))
if ano == 0:
		ano = date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} É um ano Bissexto!!!')

else:
    print(f'O ano {ano} Não é Bissexto.')