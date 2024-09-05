from time import sleep
v_casa=input('Qual é o valor da casa?') #01-Faz a pergunta do valor em STRING!!!

v_casa_convert=v_casa.replace('.','').replace(',','')#02-Substitui os pontos e vírgulas por espaços vazios
print(type(v_casa_convert))#03-Verifica qual é o typo, se é str,float...
v_casa_float=float(v_casa_convert)#04-Faz a conversão
print(type(v_casa_float))#05-Confirma se foi convertido para float
print(v_casa_float)#06-Mostra o valor final
