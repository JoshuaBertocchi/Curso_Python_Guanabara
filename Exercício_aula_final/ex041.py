

print('-=='*8, 'Nivel na Natação','==-'*8)

idade = int(input('Me informe sua idade:'))

if idade <= 9:
    print('Seu nível é Mirim')
elif (idade <= 14) and (idade >= 10):
    print('Seu nível é Infantil')
elif (idade <= 19) and (idade >= 15):
    print('Seu nível é Junior')
elif idade == 20:
    print('Seu nível é Sênior')
elif idade >= 21:
    print('Seu nível é Master')
else:
    print('erro 404')