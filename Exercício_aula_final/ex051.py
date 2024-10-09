print('-='*8, '10 Primeiros termos da PA', '=-'*8)
primeiro_termo = int(input('Me diga o Primeiro Termo:'))
termo_final = int(input('Me informe o Termo final(quantas vezes deve ser calculado): '))
razao = int(input('Me informe a Razão:'))
for i in range(1,termo_final+1):
    pa = primeiro_termo + (i - 1)*razao
    print(f'{i}. PA= {pa}')
