print('_-'*8, ': Palíndromo :', '-_'*8)

frase = str(input('Digite uma frase:')).upper()
frase= frase.split()
frase_final=''.join(frase)
invertida = frase_final[::-1]

#print(frase_final[::-1])

if invertida == frase_final:
    print('É palíndromo.')
else:
    print('Não é palídromo.')
