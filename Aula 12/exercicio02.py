from random import randint

with open ("numeros.txt", "w") as numeros:
    for _ in range(100):
        numeros.write(f"{randint(1,1000)} ")


def soma_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as arquivos:
        conteudo = arquivos.read()
        numeros = conteudo.split()
        soma = 0
        for numero in numeros:
            soma += int(numero)
        return soma
    
resultado = soma_arquivo("numeros.txt")
print(f"A soma dos números no arquivo é: {resultado}")