nome_complt=input('Escreva seu nome completo?:')
frase01=('Esse é seu nome com Upper:')

print(frase01, nome_complt.upper())
print('Esse é seu nome com Lower', nome_complt.lower())
nome_complt01=(nome_complt.split())
nome_complt02=''.join(nome_complt01)
print('Espaços totais sem contar espaços vazios:',(len(nome_complt02)))
print('Espaços primeira letra:',len(nome_complt01[0]))
