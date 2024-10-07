from random import randint

print('-_'*8,'JOGO DA ADIVINHAÇÃO!','-_'*8)
n = int(input('Qual número estou pensando, entre 0 a 10? '))
sorteio = randint(0, 10)
if n == sorteio:
    print(f'Parabéns você acertou! Número sorteado: {sorteio}')
elif n > 11:
    print('-_'*8,'APENAS DE 0 A 10!','-_'*8)

n_palpites = 1

while n != sorteio:
    n_palpites += 1
    print(f'Você errou, chute outro número')
    n = int(input('Qual número estou pensando, entre 0 a 10? '))
    if n == sorteio:
        print(f'Parabéns você acertou! Número sorteado: {sorteio}.\nN°de tentativas: {n_palpites}.')
    elif n >= 11:
        print('-_'*8,'APENAS DE 0 A 10!','-_'*8)



