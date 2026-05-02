name = input('Digite seu nome completo: ').strip()
first = name.split()[0]
last = name.split()[-1]
print(f'Primeiro nome:'
      f' {first.capitalize()} e ultimo nome: {last.capitalize()}')
