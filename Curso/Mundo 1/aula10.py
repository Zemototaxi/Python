
#Estrutura Convencional (Bloco)

#if condição:
    # Executa se a condição for verdadeira
    #bloco_true()
#else:
    # Executa se a condição for falsa
    #bloco_false()

nome = str(input('Digite seu nome: '))
if nome == 'Luiz':
    print('Que nome lindo')
else:
    print(f'Seu nome e uma merda {nome}')
print(f'Bom dia {nome}')
#Operador Ternário (Linha Única)
# Para o Python entender sua lógica em uma f-string (texto formatado), você precisa usar o operador ternário dentro das chaves {}
nome = "Luiz"
print(f"Bom dia, que nome lindo {nome if nome == 'Luiz' else 'estranho'}")
#teste 2 usando lower para formatação do nome
nome = input('Qual seu nome? ')
# O .lower() garante que "LUIZ", "luiz" ou "Luiz" virem "luiz"
print(f"Bom dia! {'Que nome lindo' if nome.lower() == 'luiz' else 'Oi'} {nome}")

#Exemplo 3O que esse código faz:
#.strip(): Se o usuário apertar espaço sem querer (" Luiz "), o Python limpa.
#.lower() == 'luiz': Não importa se ele digitou LUIZ, lUiZ ou luiz, a condição aceita.
#.capitalize(): Garante que o nome seja exibido bonito no print (Luiz), mesmo que ele tenha digitado tudo minúsculo.

nome = input('Qual seu nome? ').strip() # .strip() remove espaços extras
# Comparamos sempre em minúsculo, mas exibimos com a primeira letra maiúscula
status = 'Que nome lindo' if nome.lower() == 'luiz' else 'Bom dia'
print(f"{status}, {nome.capitalize()}!")





