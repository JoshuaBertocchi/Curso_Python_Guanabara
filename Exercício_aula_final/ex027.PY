nome=str(input('Digite seu nome completo:')).strip()
nome_list_title=nome.title()
nome_list01=nome_list_title.split()
print(f'Primeiro nome:{nome_list01[0]} \n Último nome:{nome_list01[-1]}')
