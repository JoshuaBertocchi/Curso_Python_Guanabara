print('='*20)
print(f'{'Tabuada':-^20}')
print('='*20)

cont = 0
while True:
    n = int(input('Qual valor você quer ver? '))
    cont += 1
    for i in range(1,11):
        print(f'{n} X {i} = {n*i} ')
    if n < 0:
        print('Programa Finalizado!')
        break
print('='*20)
print('TABUADA FINALIZADA!')
print('='*20)