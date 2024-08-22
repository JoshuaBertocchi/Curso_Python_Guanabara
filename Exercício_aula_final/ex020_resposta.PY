import random

qtd_alunos = int(input('Quantos alunos vamos sortear?'))
alunos = []

for _ in range(qtd_alunos):
    aluno = input(f"Informe o nome do aluno {_+1}°:")
    alunos.append(aluno)

random.shuffle(x=alunos)

for aluno in alunos:
    print(aluno)