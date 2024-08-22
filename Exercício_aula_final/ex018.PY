import math
ang=float(input('Digite um ângulo:'))
convert= math.radians(ang)
print(f'Resposta:'
      f'\n Seno:{math.sin(convert):.3f}'
      f'\n Cosseno:{math.cos(convert):.3f}'
      f'\n Tangente:{math.tan(convert):.3f}')
