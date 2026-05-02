from random import randint
from cores import R, RESET as X
# O computador "pensa" em um número
computer = randint(1, 5)
# O usuário tenta adivinhar
num = int(input('Digite um numero de 1 a 5: '))
# Erro corrigido: Use "=" para atribuir valor, não "=="
if num == computer:
    print(f'Parabens voce acertou! eu pensei em {computer}')
else:
    print(f'{R}Tente novamente, eu pensei no numero{X} {computer}')