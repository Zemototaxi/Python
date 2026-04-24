import pandas as pd
from datetime import datetime

# 1. Coleta os dados
pedido = input("Número do pedido: ")
qtd = int(input("Quantidade: "))
horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# 2. Organiza em um dicionário
novo_registro = {"Horário": [horario], "Pedido": [pedido], "Qtd": [qtd]}

# 3. Transforma em "planilha" e salva
df = pd.DataFrame(novo_registro)
df.to_csv("saidas.csv", mode='a', index=False, header=False)

print("Dados salvos com sucesso!")

