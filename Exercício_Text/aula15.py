nome = str(input('Qual é seu nome:  ')).title()
for i in nome:
    print(f'{i:-^20}', end='')
print('\nLi seu nome todo!')