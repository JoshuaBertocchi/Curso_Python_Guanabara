import math,emoji
print(emoji.emojize(':triangular_ruler:'*1))
cat = float(input('Digite o valor do cateto oposto:'))
adja = float(input('Digite o valor do cateto adjacente:'))
poten_soma = math.sqrt(cat**2 + adja**2)
print(emoji.emojize(f'Valor hipotenusa:{poten_soma:.2f} :triangular_ruler:'))
print(emoji.emojize(':triangular_ruler:'*1))