from time import sleep
import random

print('--='*8, 'Pedra, Papel e Tesoura!', '=--'*8)

pedra = """
    _______ Pedra
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
papel = """
     _______ Papel
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
tesoura = """
    _______ Tesoura
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

lista=[pedra, papel, tesoura]
print('--='*8,'Vamos ver quem ganha!','--='*8)
pergunta=int(input('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
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
if escolha_maquina == 0:
    if escolha_usuario == 0:
        print('Empate')
    elif escolha_usuario == 1:
        print('JOGADOR VENCEU')
    elif escolha_usuario == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif escolha_maquina == 1:
    if escolha_usuario == 1:
        print('Empate')
    elif escolha_usuario == 0:
        print('JOGADOR VENCEU')
    elif escolha_usuario == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif escolha_maquina == 2:
    if escolha_usuario == 2:
        print('Empate')
    elif escolha_usuario == 0:
        print('JOGADOR VENCEU')
    elif escolha_usuario == 1:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

