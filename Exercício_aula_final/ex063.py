
print('_-'*20,'Sequência de Fibonacci', '-_'*20)
n = int(input('Me diga quantos termos você quer ver?'))
#! Os termos inicias sempre seram esses!!!
termo_1= 0
termo_2= 1
cont = 3 # O contador conta apartir do 3, porque já possui 2 temos salvos no código, o termo_1 e termo_2
print(f' {termo_1} => {termo_2} =>' , end='') # imprime os primeiros 2 termos 
while cont <= n: 
    termo_3= termo_1 + termo_2
    print(f' {termo_3} =>', end= '')
    termo_1 = termo_2
    termo_2 = termo_3
    cont += 1
    
    
print('Fim')