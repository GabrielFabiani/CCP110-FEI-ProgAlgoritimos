# Faça um programa que cria uma matriz M 10 X 15, sendo que cada
# elemento é um inteiro gerado aleatoriamente.
# Então, exiba a matriz completa e, na sequência, somente os
# elementos da primeira coluna da matriz.
# Exemplo de execução:
from random import randint
def gerar_matriz(n_linhas, n_colunas):
    M = []
    for num_linha in range(n_linhas):
        linha = []
        for num_coluna in range(n_colunas):
            linha.append(randint(0,100))
        M.append(linha)
    return M

def imprimir_matriz():
    for linha in range(len(M)):
        for coluna in range(len(M[linha])):
            print(f"{M[linha][coluna]:4}", end="")
        print()
        

M = gerar_matriz(10,15)
imprimir_matriz(M)

print("------------------------------------------")
for linha in range (len(M)):
    print(M[linha][0])