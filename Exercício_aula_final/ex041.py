
from datetime import date
print('-=='*8, 'Nivel na Natação','==-'*8)

ano = int(input('Me seu ano de nascimento:'))
idade = date.today().year - ano

if idade <= 9:
    print(f'Seu nível é Mirim, Idade:{idade}')
elif (idade <= 14) and (idade >= 10):
    print(f'Seu nível é Infantil, Idade:{idade}')
elif (idade <= 19) and (idade >= 15):
    print(f'Seu nível é Junior, Idade:{idade}')
elif idade <=25:
    print(f'Seu nível é Sênior, Idade:{idade}')
elif idade >=26:
    print(f'Seu nível é Master, Idade:{idade}')
else:
    print(f'erro 404')