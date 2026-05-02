from cores import C, RESET

km = float(input('Quantos KM pecorreu '))
dias = int(input('Por quantos dias '))
valor_dia = dias*60
valor_km = km*0.15
print(f'Valor por KM rodados R${valor_km:.2f},'
      f' \nValor por dias alugados R${valor_dia:.2f}'
      f' \nValor total {C}R${valor_dia+valor_km:.2f}{RESET}')