import random , emoji

print("(",'='*30,'Vamos ver quem ganha!!!', '='*30,')')

num=[0,1,2,3,4,5]
#num=list(range(0,10,2))

num_maquina=int(random.choice(num))

num_use=int(input('Estou pensando em um número de 0 a 5, qual será?'))

if num_maquina == num_use:
    print(emoji.emojize(f'Parabéns :smile: você acertou!!!!\n O número foi {num_maquina}', language='alias'))
else:
    print(f'Você errou, o número é: {num_maquina}')