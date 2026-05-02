n = input('Digite um numero ').zfill(4)
print(f'unidade {n[3]}')
print(f'dezena {n[2]}')
print(f'centena {n[1]}')
print(f'milhar {n[0]}')


#Forma avançada»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»


num = int(input('\n1Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

