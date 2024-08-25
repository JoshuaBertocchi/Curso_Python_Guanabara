nome=input('Qual é o seu nome completo?')
#01- Pergunta o nome
convert_cap=nome.title()  
#02- Converte em title
res=('Silva' in convert_cap)
#03- Pergunta se possuí Silva dentro de convert_cap
print(f'Esse nome possui Silva?: {res}')
#04- Da a resposta