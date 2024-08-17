try:
    print('=' * 60)
    day = int(input('Quantos dias você ficou com o carro?'))
    print('=' * 60)
    km=float(input('Quantos Km você percorreu?'))
    print('=' * 60)
    v_day= day*60
    v_km= km*0.15
    v_total=v_day+v_km
    print(f'O valor a ser pago por dia é:{v_day:.2f}\n O valor a ser pago por Km é:{v_km:.2f}\n Valor total:{v_total:.2f}')
    print('=' * 60)
except:
    print('Xx'*90)
    print('Apenas números!!!')
    print('Xx' * 90)
