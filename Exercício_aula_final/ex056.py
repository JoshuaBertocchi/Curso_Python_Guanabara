soma_mulheres = 0
soma_idade = 0
lista_geral = []
for i in range(0,5):
    print(f'{i+1}. Pessoa')
    nome = str(input('Me informe seu nome: ')).title()
    idade = int(input('Me informe sua idade: '))
    sexo = str(input('Me informe seu sexo: ')).title()
    lista_geral.append([nome, idade, sexo])
    soma_idade += idade
    if sexo == 'Feminino':
        soma_mulheres += 'Feminino'


idade_0usuario = int(lista_geral[0][1])
idade_1usuario = int(lista_geral[1][1])
idade_2usuario = int(lista_geral[2][1])
idade_3usuario = int(lista_geral[3][1])
idade_4usuario = int(lista_geral[4][1])

calculo_media_idade = (idade_0usuario + idade_1usuario + idade_2usuario + idade_3usuario + idade_4usuario)/5

print(f'Esse é o resultado da média da idade do grupo: {calculo_media_idade}')
print(lista_geral[0][0])
print(lista_geral)
