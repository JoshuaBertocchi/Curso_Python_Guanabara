import random

print('='*20)
print(f'|{'|Impar ou PAR|':=^18}|')
print('='*20)
escolha = ''
escolha_maquina = ''
cont_vitoria= 0 
while True:
    escolha = str(input('Qual você escolhe Par ou Impar? P ou I ')).upper()
    escolha_maquina = 'P' if escolha == 'I' else 'I'
    escolha_n = int(input('Informe seu número: '))
    n_maquina = random.randint(0,10)
    conta = (escolha_n + n_maquina)%2
    if (conta == 0 and escolha == 'P') or (conta == 1 and escolha == 'I'):
        cont_vitoria += 1
        print(f'Você ganhou!\nEscolha final: {'Par' if escolha == 'P' else 'Impar'}')
    else: 
        print('Você perdeu!')
        break
print(f'Quantidade de vitórias: {cont_vitoria}')
print(f'Quantidade de Tentativas: {cont_vitoria + 1}')
    



