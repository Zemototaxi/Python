tradutor = {True: "Sim", False: "Não"}
city = input('Qual o nome da sua cidade? ').strip()
ct = city[:5].upper() == 'SANTO'
print(f'Sua cidade começa com SANTO? {tradutor[ct]}')