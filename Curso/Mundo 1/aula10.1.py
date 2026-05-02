nome ,n1, n2 = input('Qual o seu nome?'), float(input('Primeira nota ')), float(input('Segunda nota '))
print(f'Ola {nome.capitalize()} a sua media foi {(n1 + n2) / 2:.1f}. {'Continue assim!!'if (n1 + n2) / 2 >=6 else 'Precisa melhorar!!'} ')

nome = input('Qual o seu nome? ').strip().capitalize()
n1 = float(input('Primeira nota : '))
n2 = float(input('Segunda nota : '))

# Validação: só calcula se as notas forem reais
if 0 <= n1 <= 10 and 0 <= n2 <= 10:
    media = (n1 + n2) / 2

    # Definindo as cores (padrão ANSI)
    verde = '\033[32m'
    vermelho = '\033[31m'
    reset = '\033[m'

    status = f'{verde}Continue assim!!' if media >= 6 else f'{vermelho}Precisa melhorar!!'

    print(f'Olá {nome}, sua média foi {media:.1f}. {status}{reset}')
else:
    print('\033[31mErro: As notas devem estar entre 0 e 10!\033[m')
