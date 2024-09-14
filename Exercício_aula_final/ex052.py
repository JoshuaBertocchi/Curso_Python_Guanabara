

print('-=-'*8, 'Números Primos', '-=-'*8)
#* 01. Pergunta o número.
num_int = int(input('Me diga um número inteiro:'))
#* 02. (count = 0) Contador usado para contar quantos restos da dívisão possuem dentro do for i in.
count = 0
#* 03. Faz a divisão/contagem até o número informado pelo usuário.
for i in range(1,num_int+1):
    #* 04. Faz o calculo do resto da divisão
    cal_01 = num_int % i
    #* 05. Pega apenas o resultado igual a zero.
    if cal_01 == 0:
        #*06. Faz a contagem de quantos 0 possuem
        count += 1
#* 07. Se a contagem de zeros for igual a 2, será um número primo!

if count == 2:
    print(f'{num_int} é um número PRIMO!')
#* 08. Caso possua mais de 3 zeros, não é número primo.
else:
    print('Não é um número PRIMO!')
