
v=int(input('Diga quantos Km são sua viagem:'))

if v >=200:
    v_maior=(v-200)*0.45
    print(f'Sua viagem é maior que 200km a taxa será:R${v_maior:.2f}!')
else:
    v_menor=v*0.50
    print(f'Sua viagem é menor que 200km a taxa será: R${v_menor:.2f}!')