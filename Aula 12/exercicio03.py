from random import randint
def gerar_numeros():
    with open ("numeros.txt", "w") as numeros:
        for _ in range(100):
            numeros.write(f"{randint(1,1000)} ")

def ler_numeros():
    with open ("numeros.txt", "w") as numeros:
        conteudo = numeros.readlines()
    
    num = []
    for linha in conteudo:
        num.append(int(linha.strip()))
    return num

gerar_numeros()
numeros_lidos = ler_numeros()
print(f"Números lidos no arquivo: {numeros_lidos}")