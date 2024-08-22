import random
aluno01=input('Nome do primeiro aluno:')
aluno02=input('Nome do segundo aluno:')
aluno03=input('Nome do terceiro aluno:')
aluno04=input('Nome do quarto aluno:')
alunos=[aluno01,aluno02,aluno03,aluno04]
sorteio= random.choice(alunos)
print(f'O aluno sorteado foi {sorteio}')
