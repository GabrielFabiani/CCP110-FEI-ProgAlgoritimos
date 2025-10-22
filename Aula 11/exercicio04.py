# Crie uma função que retorna o número de caracteres únicos em
# uma string criada pelo usuário.
# Por exemplo:
# “Hello, World!” tem 10 caracteres únicos
# enquanto zzz tem somente 1 caractere único.
# Use um dicionário para resolver este problema.

palavra = input("Digite uma palavra: ")
dicionario = {}
for letra in palavra:
    if letra in dicionario:
        dicionario[letra] + 1
    else:
        dicionario[letra] = 1
    
print(dicionario)
print(len(dicionario))
