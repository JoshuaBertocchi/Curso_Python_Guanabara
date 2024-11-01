import random
from time import sleep

escolha = ''
escolha_maquina = ''
cont_vitoria= 0 
while True:
    
    try:
        print('='*20)
        print(f'|{'|Impar ou PAR|':=^18}|')
        print('='*20)
        escolha = str(input('Qual você escolhe Par ou Impar? P ou I ')).upper()
        if escolha != 'P' and escolha != 'I':
            print('Escolha apenas P ou I!!!')
            continue
        escolha_maquina = 'P' if escolha == 'I' else 'I'
        escolha_n = int(input('Informe seu número: '))
        n_maquina = random.randint(0,10)
    except:
        print('Informe apenas números inteiros!!!')
        continue
    conta = (escolha_n + n_maquina)%2
    
    if (conta == 0 and escolha == 'P') or (conta == 1 and escolha == 'I'):
        sleep(1)
        cont_vitoria += 1
        print('='*20)
        print(f'Você ganhou!\nSua Escolha: {escolha_n}\nEscolha máquina: {n_maquina}\nResultado final: {'DEU PAR' if (escolha_n + n_maquina)%2 == 0 else 'DEU IMPAR'}')
        
    else:
        sleep(1)
        print('='*20)
        print('Você perdeu!')
        print('='*20)
        break
    sleep(1)
sleep(1)
print('DEU PAR' if (escolha_n + n_maquina)%2 == 0 else 'DEU IMPAR')
print(f'Sua Escolha: {escolha_n} Escolha máquina: {n_maquina}, Soma final: {escolha_n + n_maquina}')
print(f'Quantidade de vitórias: {cont_vitoria}')
print(f'Quantidade de Tentativas: {cont_vitoria + 1}')