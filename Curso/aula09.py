import emoji

frase = 'curso em video Python          '

# Fatiamento
print(f'Fatiamento [3:15]: "{frase[3:15]}"')
print(f'Tamanho total da string: {len(frase)}')

# Análise
# Corrigi a sintaxe do count com intervalo: count('caractere', início, fim)
print(f'Quantas vezes aparece "e" entre 0 e 13: {frase.count("e", 0, 13)}')
print(f'Quantas vezes aparece "e" no total: {frase.count("e")}')

# Transformação
print(f'Tudo em maiúsculo: {frase.upper()}')
print(f'Tudo em minúsculo: {frase.lower()}')
print(f'Trocando Python por Android: {frase.replace("Python", "Android")}')
print(f'Posição onde começa "deo": {frase.find("deo")}')
print(f'Só a primeira letra maiúscula: {frase.capitalize()}')
print(f'Iniciais em maiúsculo (Título): {frase.title()}')
print(f'Existe a palavra "curso" na frase? {"curso" in frase}')

# Limpeza de espaços
print(f'Tamanho original: {len(frase)}')
print(f'Tamanho após o strip (remover espaços): {len(frase.strip())}')

# Divisão e Junção
lista_palavras = frase.split()
print(f'Frase dividida em lista: {lista_palavras}')
print(f'Juntando a lista com hífen: {"-".join(lista_palavras)}')



print("""\nFatiamento ([3:15]): Pega do caractere 3 até o 14. Resulta em "so em video ".\n
Análise (count): Conta quantas vezes a letra "e" aparece. Note que frase.count('e,0,13') daria erro, o correto para limitar o espaço é frase.count('e', 0, 13).\n
Transformação:
replace: Troca palavras (mas só exibe, não altera a variável original a menos que você faça frase = frase.replace(...)).
strip: Remove os espaços inúteis no final (espaços em branco que você deixou na declaração da variável).\n
Divisão e Junção:
split(): Transforma a frase em uma lista de palavras: ['curso', 'em', 'video', 'Python'].
join(): Junta os elementos. O seu último comando '-'.join(frase.split()) é a forma perfeita de criar "slugs" (links), resultando em curso-em-video-Python.""")
print(emoji.emojize(':polegar_para_cima: ', language='pt'))

