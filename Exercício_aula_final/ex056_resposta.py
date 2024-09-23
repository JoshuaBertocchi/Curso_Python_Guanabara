qtd_pessoas = 4
soma_idade = 0
cont_mulheres= 0 # contador mulheres menores que 20 anos
maioridadehomem = 0
nomemaisvelho = ''
for i in range(1,5):
    print(f'----- {i}° Pessoa -----')
    nome = str(input('Qual é seu nome: ')).title()
    idade = int(input('Qual é sua idade: '))
    sexo = str(input('Qual e seu sexo [M/F]: ')).upper()

    soma_idade += idade
    media_idade = soma_idade/ qtd_pessoas
    if i == 1 and sexo == 'M':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'F':
        if idade < 20:
            cont_mulheres += 1

print(f'A média de idade do grupo é {media_idade:.2f}')
print(f'Mulheres com menos de 20 anos: {cont_mulheres}')
print(f'Nome do homem mais velho é {nomemaisvelho}.')

