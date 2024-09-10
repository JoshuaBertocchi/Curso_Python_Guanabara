from time import sleep
print('=$='*8,'Banco do Bertocchi','=$='*8)

print('Seja bem-vindo ao banco!!!')

v_casa=str(input('Qual é o valor da casa? R$:'))
v_casa_convert=v_casa.replace('.','').replace(',','')
v_casa_final=float(v_casa_convert)
print('Captando Dados, Só um momento...')
sleep(1)

salário=str(input('Quanto você recebe por mês?R$:'))
salário_convert=salário.replace(',','').replace('.','')
salário_final=float(salário_convert)
print('Salvando Dados, Só um momento...')
sleep(1)

ano=float(input('Quantos anos você pretende pagar?'))
sleep(1)

#calculo prestação
valor_30=((salário_final*30)/100)
calculo_mês=ano*12
calculo_parcelas=v_casa_final/calculo_mês

print(f'Valor 30%: {valor_30:.2f}, N° de meses:{calculo_mês:.2f}, Valor das parcelas. R$:{calculo_parcelas:.2f}')

if calculo_parcelas < valor_30:
    print(f'Parabéns, vocês foi aprovado!!! O valor da parcela será R$:{calculo_parcelas:.2f}')

else:
    print('Empréstimo NEGADO!')

