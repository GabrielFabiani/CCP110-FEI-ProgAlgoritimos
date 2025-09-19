num_linhas = int(input("Digite o número de linhas: "))
num_colunas = int(input("Digite o número de colunas: "))
for i in range(num_linhas):
    for j in range(num_colunas):
        if (i > j) or (i==j):
            print("$", end = "")
        else:
            print("@", end="")
    print()