trip = (int(input('Qual a distancia da sua viagem: ')))
if trip <= 200:
    print(f'Sua passagem custa R${trip * 0.50:.2f}')
else:
    print(f'Sua passagem custa R${trip * 0.45:.2f}!')
