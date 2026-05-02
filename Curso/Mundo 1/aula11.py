#\033[Estilo;CorTexto;CorFundo m
#\033[0:33:44m

print('\033[97;41mTexto Branco Fundo vermelho \033[0m')

print('\033[1;4;33;44m TEXTO SUBLINHADO AMARELO COM FUNDO AZUL\033[m')

print('\033[1;35;43m TEXTO ROXO EM NEGRITO COM FUNDO AMARELO\033[m')

print('\033[97;42m TEXTO BRANCO COM FUNDO VERDE \033[m')

print('\033[37;40mTEXTO CINZA FUNDO PRETO\033[m')

print('\033[1;7;97mTEXTO CORES IVERTIDAS\033[m')

# Cores de texto comuns
print(f"\033[31mEste texto é vermelho\033[0m")
print(f"\033[32mEste texto é verde\033[0m")
print(f"\033[34mEste texto é azul\033[0m")
# Texto com fundo (Branco com fundo roxo)
print(f"\033[0;45mTexto branco, fundo roxo\033[0m")

import os

print("\n--- TABELA DE CORES ANSI (INCLUINDO BRANCO INTENSO) ---")

# Adicionamos o 37 (Cinza) e o 97 (Branco Brilhante) à lista de textos
codigos_texto = list(range(30, 38)) + [97]
# Adicionamos o 47 (Cinza) e o 107 (Branco Brilhante) à lista de fundos
codigos_fundo = list(range(40, 48)) + [107]

for fundo in codigos_fundo:
    for texto in codigos_texto:
        # Usamos 1; para garantir que o branco seja "natural" e vivo
        print(f"\033[1;{texto};{fundo}m {texto};{fundo} \033[m", end="")
    print()
