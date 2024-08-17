try:
    c = float(input('Me diga o valor em °C:'))
    convertido = ((c * 9) / 5) + 32
    print(f'Esse é o valor final:{convertido}°F')

except:
    print('='*40)
    print('Apenas números e (.)cabeça!!!')
    print('='*40)