n1=int(input('Digite um valor:'))
n2=int(input('Digite outro valor:'))
s=n1+n2
sub=n1-n2
m=n1*n2
d=n1/n2
p=n1**n2
div=n1//n2
res=n1%n2
print(f'A soma é: {s}\n O Produto é {m}\n A Divisão é: {d:.3f}\n A Potência é: {p}', end=' ___ ')
print(f'Divisão inteira é: {div:.3f}\n Resto da divisão: {res}')