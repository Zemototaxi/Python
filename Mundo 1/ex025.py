tradutor = {True: "Sim", False: "Não"}
name = input('Qual o seu nome? ').strip()
nome = 'SILVA' in name[0:].upper()
print(f'Seu nome tem Silva? {tradutor[nome]}')