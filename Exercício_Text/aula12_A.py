nome = str(input('Qual é seu nome?'))
if nome == 'Joshua':
    print('Que nome lindo!!!')
elif nome == 'Isabelle' or nome == 'Mario' or nome == 'Julia' or nome == 'Bruno' or nome == 'João':
    print('Nome comum!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Nome legal.')
print('Seja Bem Vindo(a)!')