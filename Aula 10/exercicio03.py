from random import randint
def gerar_matriz(n_linhas, n_colunas):
    M = []
    for num_linhas in range(n_linhas):
        linha = []
        for num_colunas in range(n_colunas):
            valor = int(input(""))
            linha.append(randint(0,100))
        M.append(linha)
    return M

def imprimir_matriz(M):
    for linha in range(len(M)):
        for coluna in range(len(M[linha])):
            print(f"{M[linha][coluna]:4}", end="")
        print()
        

def soma_diagonal_principal(M):
    soma = 0
    for linha in range(len(M)):
        for coluna in range(len(M[linha])):
            if linha == coluna:
                soma += M[linha][coluna]
    return soma
    

M = gerar_matriz(10,15)
imprimir_matriz(M)
print(f"A soma da diagonal principal é: {soma_diagonal_principal(M)}")
