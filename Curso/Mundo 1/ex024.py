from cores import G, R, RESET as X

tradutor = {
    True: f"{G}Sim{X}",
    False: f"{R}Não{X}"
}

city = input('Qual o nome da sua cidade? ').strip()

ct = city[:5].upper() == 'SANTO'

print(f'Sua cidade começa com SANTO? {tradutor[ct]}')