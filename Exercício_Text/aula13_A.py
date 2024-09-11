from time import sleep
tempo = 1
for o in range(10, 0, -1): #01-Valor maior primeiro e -1 no final, conta de trás para frente.
    sleep(tempo)
    tempo = tempo - 0.1
    print(o)
print('Fim')
