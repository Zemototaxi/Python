from cores import R,W , RESET as X

km = float(input('Qual a sua velocidade em KM: '))

multa = (km - 80) * 7

if km > 80:
    print(f'{R}Voce sera multado em R${multa}{X}')
else :
    print(f'{W}Continue abaixo do limite{W}')