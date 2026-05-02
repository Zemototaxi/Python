import random

a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')

# O sorteio direto na f-string
print(f'O aluno sorteado é {random.choice([a, b, c, d])}')

import random

alunos = []

while True:
    nome = input('Digite o nome do aluno (ou "fim" para sortear): ')

    if nome.lower() == 'fim':
        break

    alunos.append(nome)

# Verifica se a lista não está vazia antes de sortear
if alunos:
    sorteado = random.choice(alunos)
    print(f'\nParticipantes: {", ".join(alunos)}')
    print(f'🏆 O aluno sorteado foi: {sorteado}')
else:
    print('Nenhum aluno foi cadastrado.')

