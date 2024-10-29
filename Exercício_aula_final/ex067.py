print('='*20)
print(f'{'Tabuada':-^20}')
print('='*20)
n = int(input('Qual valor você quer ver? '))
cont = 0
while cont <=10:
    cont += 1
    print(f'{n} X {cont} = {n*cont} ')
    if cont == 10:
        cont = 0
        n = int(input('Qual valor você quer ver? '))
    if n < 0:
        print('Programa Finalizado!')
        break
print('TABUADA FINALIZADA!')