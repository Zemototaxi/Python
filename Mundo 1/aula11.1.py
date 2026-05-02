a = 2
b = 3
print(f'Os valores \033[31m{a}\033[m + \033[36m{b}\033[m sao = \033[35m{a+b}\033[m !!!!\n')
#Limpeza: Se você for usar isso muitas vezes, pode criar variáveis curtas para as cores
R = '\033[31m' # Red
C = '\033[36m' # Cyan
P = '\033[35m' # Purple
X = '\033[m'   # Reset

print(f'Os valores {R}{a}{X} + {C}{b}{X} sao = {P}{a+b}{X} !!!!')

