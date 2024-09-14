print('-='*8, '10 Primeiros temos da PA', '=-'*8)
primeiro_termo = int(input('Me diga o Primeiro Termo:'))
termo_final = int(input('Me informe o Termo final(quantas vezes deve ser calculado): '))
razão = int(input('Me informe a Razão:'))
for i in range(1,termo_final+1):
    pa = primeiro_termo + (i - 1)*razão
    print(f'{i}. PA= {pa}')
