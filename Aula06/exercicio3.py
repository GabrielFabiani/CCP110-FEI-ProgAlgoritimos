num_linhas = int(input("Digite o número de linhas: "))
num_colunas = int(input("Digite o número de colunas: "))
for i in range(num_linhas):
    for j in range(num_colunas):
        if (i % 2 == 0 and j % 2 ==0) or (i % 2 == 0 and j % 2 ==0):
            print("*", end = "")
        else:
            print("#", end="")
    print()