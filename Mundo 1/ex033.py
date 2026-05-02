# Lê a linha, divide pelos espaços e converte cada parte para inteiro
numeros = [int(x) for x in input(
    'Digite três números separados por espaço: '
).split()]
print(f'Maior: {max(numeros)}')
print(f'Menor: {min(numeros)}')
