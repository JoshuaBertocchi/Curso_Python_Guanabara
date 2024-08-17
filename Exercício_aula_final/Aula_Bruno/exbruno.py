while True:
    try:
        altura = float(input('Digite a altura: '))
        largura = float(input('Digite a largura: '))

        # Calcula a área
        m3 = altura * largura

        # Exibe o valor da área
        if m3.is_integer():
            print(f'Esse é o valor {int(m3)} m²')
        else:
            print(f'Esse é o valor {m3:.2f} m²')



    except ValueError:
        print("Informe apenas números.")
