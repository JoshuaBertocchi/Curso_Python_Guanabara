peso = float(input('Me diga seu, KG:'))
altura = float(input('Me diga sua altura. m:'))

imc = (peso/(altura**2))
print(f'Seu imc é: {imc:.2f}')

if imc < 18.5:
    print('Faixa de peso: Abaixo do Peso')
elif imc > 18.5 and imc < 25:
    print('Faixa de peso:Peso ideal')
elif imc > 25 and imc < 30:
    print('Faixa de peso:Sobrepeso')
elif imc > 30 and imc < 40:
    print('Faixa de peso:Obesidade')
elif imc > 40:
    print('Faixa de peso:Obesidade mórbida')
else:
    print('Faixa de peso:Algo deu errado...')