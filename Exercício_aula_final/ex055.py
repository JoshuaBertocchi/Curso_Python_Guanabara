
pessoas = int(input('Quantas pessoas vão informar o peso?'))
lista_kg = []

for i in range(1,pessoas+1):

    kg = float(input(f'{i}. Me diga o seu peso. KG:'))
    lista_kg.append(kg)
    lista_kg.sort()

print(f' Esse foi o maior peso. KG:{lista_kg[-1]:.2f}')
print(f' Esse foi o menor peso. KG:{lista_kg[0]:.2f}')
