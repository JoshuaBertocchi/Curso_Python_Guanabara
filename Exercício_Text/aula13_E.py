s = 0
for c in range(0, 4):
    n = int(input('Digite um valor:'))
    s = s + n
    #* ou (s += n)
print(f'A soma é igual a :{s}')