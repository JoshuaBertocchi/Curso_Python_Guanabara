from time import sleep
import random

print('--='*8, 'Pedra, Papel e Tesoura!', '=--'*8)

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

lista=[pedra, papel, tesoura]
print('--='*8,'Vamos ver quem ganha!','--='*8)
pergunta=int(input('''0. Pedra
1. Papel
2. Tesoura
Digite o número:'''))

escolha_maquina=random.choice(lista)
escolha_usuario = lista[pergunta]
print('Pedra...')
sleep(0.5)
print('Papel...')
sleep(0.4)
print('Tesoura...')
sleep(0.3)
print('Carregando...')
sleep(0.2)

print(f'Escolha máquina: {escolha_maquina}')
print(f'Sua escolha: {escolha_usuario}')
sleep(1)
if escolha_usuario == lista[0] and escolha_maquina == lista[2]:
    print('Usuário ganhoouu!!!')
elif escolha_usuario == lista[2] and escolha_maquina == lista[1]:
    print('Usuário ganhoouu!!!')
elif escolha_usuario == lista[1] and escolha_maquina == lista[0]:
    print('Usuário ganhoouu!!!')
elif escolha_usuario == escolha_maquina:
    print(' O jogo empatou!!!')
else:
    print('A máquina ganhou!!!')