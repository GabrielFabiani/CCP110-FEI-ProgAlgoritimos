# Faça um programa que cria uma matriz M 10 X 15, sendo que cada
# elemento é um inteiro gerado aleatoriamente.
# Então, exiba a matriz completa e, na sequência, somente os
# elementos da primeira coluna da matriz.
# Exemplo de execução:

M = []

for num_linha in range(10):
    linha = []
    for num_coluna in range(15):
        linha.append(num_linha + num_coluna)
    M.append(linha)
