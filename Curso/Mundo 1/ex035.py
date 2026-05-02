l1 = int(input('Digite o primeiro valor: '))
l2 = int(input('Digite o segundo valor: '))
l3 = int(input('Digite o terceiro valor: '))

# Regra: Cada lado deve ser menor que a soma dos outros dois
if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    print(f'Pode formar um triangulo')
else:
    print(f'Nao pode formar um triangulo')