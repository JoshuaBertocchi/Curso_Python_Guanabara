
medida_a=float(input('Me diga a 1° médida do triângulo:'))
medida_b=float(input('Me diga a 2° médida do triângulo:'))
medida_c=float(input('Me diga a 3° médida do triângulo:'))

if (medida_a + medida_b >= medida_c) and (medida_b + medida_c >= medida_a) and (medida_c + medida_a>= medida_b):
    print('O triângulo será formado')


else:
    print('O triângulo NÃO será formado')
