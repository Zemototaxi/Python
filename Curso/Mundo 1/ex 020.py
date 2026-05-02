import random

a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))

lista = [a, b, c, d]
random.shuffle(lista)

# Usando f-string com join para uma leitura mais limpa
print(f'A ordem sorteada foi: {", ".join(lista)}')
