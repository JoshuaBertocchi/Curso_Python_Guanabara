from time import sleep
medida_a=float(input('Me diga a 1° médida do triângulo:'))
medida_b=float(input('Me diga a 2° médida do triângulo:'))
medida_c=float(input('Me diga a 3° médida do triângulo:'))

if (medida_a + medida_b >= medida_c) and (medida_b + medida_c >= medida_a) and (medida_c + medida_a>= medida_b):
    print('O triângulo será formado')
else:
    print('O triângulo não será formado!')

sleep(0.5)
print('Aguarde...')
sleep(3)

if (medida_a == medida_b) and (medida_a == medida_c):
    print('Ele possui seu lados todos iguais. É um triângulo EQUILÁTERO.')
elif (medida_a == medida_b !=medida_c) or (medida_b == medida_c !=medida_a) or (medida_c == medida_a !=medida_b):
     print('Ele possui apenas 2 lados iguais. É um triângulo ISÓSCELES.')
elif(medida_a != medida_b) and (medida_b != medida_c) and (medida_c != medida_a):
    print('Todos os lados são diferentes. É um triângulo Escaleno. ')

else:
    print('Algo deu errado...')