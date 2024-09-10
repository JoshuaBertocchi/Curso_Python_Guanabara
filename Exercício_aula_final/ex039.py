from datetime import date

print('-=='*8,'Alistamento Militar','==-'*8)

ano = int(input('Me informe em qual ano você nasceu?'))

ano_atual=date.today().year
ano_convert= int(ano_atual)
calculo_idade= ano_convert - ano
calculo_falta= 18 - calculo_idade #CALCULO de quantos anos faltam para se alistar
calculo_passou= calculo_idade - 18 #CALCULO de quantos anos passaram

if calculo_idade < 18:
    print(f'Ainda não chegou a hora, faltam {calculo_falta} anos, em {ano_convert + calculo_falta}.')
elif calculo_idade > 18:
    print(f'Seu alistamento já passou, foi a {calculo_passou} anos atrás, em {ano_convert - calculo_passou }.')
elif calculo_idade == 18:
    print(f'Você possui {calculo_idade} anos, está no ano do seu alistamento!')
else:
    print('Algo deu errado, tente novamente!')
