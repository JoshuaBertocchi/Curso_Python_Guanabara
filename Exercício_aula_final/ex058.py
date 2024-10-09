from random import randint

print('-_'*8,'JOGO DA ADIVINHAÇÃO!','-_'*8)

sorteio = randint(0, 10)
n_palpites = 0
acertou = False
while not acertou:
    n_palpites += 1
    n = int(input('Qual número estou pensando, entre 0 a 10? '))
    if n == sorteio:
        acertou = True 
        3 
    if n >= 11:
        print('-_'*8,'APENAS DE 0 A 10!','-_'*8)
    else:
        if n > sorteio:
            print('Menos... Tente mais uma vez.')
        elif n < sorteio: 
            print('Mais... Tente mais uma vez.')

print(f'Parabéns você acertou! Número sorteado: {sorteio}.\nN°de tentativas: {n_palpites}.')


