nome = input('Digite seu nome completo: ')

print(f'Maiúsculo: {nome.upper()}')
print(f'Minúsculo: {nome.lower()}')

# Conta o total sem os espaços do início/fim
print(f'Total com espaços internos: {len(nome.strip())}')

# Conta APENAS as letras (remove todos os espaços)
letras_apenas = len(nome.replace(' ', ''))
print(f'Total de letras (sem espaços): {letras_apenas}')

# Pega o primeiro nome e conta as letras dele
primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras')

