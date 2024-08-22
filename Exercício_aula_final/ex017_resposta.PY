import math, emoji
print(emoji.emojize(':triangular_ruler:'*20))
cat = float(input('Digite o valor do cateto oposto:'))
adja = float(input('Digite o valor do cateto adjacente:'))
hi = math.hypot(cat, adja)
print(emoji.emojize(f'Valor hipotenusa:{hi:.2f} :triangular_ruler:'))
print(emoji.emojize(':triangular_ruler:'*20))