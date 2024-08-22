import random


aluno01=input('Nome do 1° aluno:')
aluno02=input('Nome do 2° aluno:')
aluno03=input('Nome do 3° aluno:')
aluno04=input('Nome do 4° aluno:')

alunos= [aluno01, aluno02, aluno03, aluno04]
random.shuffle(x=alunos)

print(f'1°Aluno:{alunos[0]}\n'
      f'2°Aluno:{alunos[1]}\n'
      f'3°Aluno:{alunos[2]}\n'
      f'4°Aluno:{alunos[3]}')