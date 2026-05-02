Payment = float(input('Digite o valor do seu salario: '))
if Payment >=1250:
    print(f'Seu aumento sera de {Payment * 0.10}')
else:
    print(f'Seu aumento sera de {Payment * 0.15}')