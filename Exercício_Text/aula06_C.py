p=input('Digite algo na tela:')
print('1-É do tipo primitivo', type(p))
print('2-Possui apenas números?',p.isnumeric())
print('3-Possui apenas letras?' ,p.isalpha())
print('4-Possui letras ou números?',p.isalnum())
print('5-Possui todas as palavras em maiúsculo?',p.isupper())
print('6-Possui a primeira palavra maiúscula e o restante minúsculas?',p.istitle())


