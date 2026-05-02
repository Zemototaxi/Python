linha1= input().split()
codigo1 = int(linha1[0])
qtd1 = int(linha1[1])
preco1 = float(linha1[2])

linha2= input().split()
codigo2 = int(linha2[0])
qtd2 = int(linha2[1])
preco2 = float(linha2[2])

print(f'VALOR A PAGAR: R$ {(qtd1 * preco1 )+(qtd2 * preco2):.2f}')