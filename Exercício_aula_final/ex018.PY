from math import radians, sin, cos, tan
ang=float(input('Digite um ângulo:'))
convert=radians(ang)
print(f'Resposta:'
      f'\n Seno:{sin(convert):.3f}'
      f'\n Cosseno:{cos(convert):.3f}'
      f'\n Tangente:{tan(convert):.3f}')
