num_linhas = int(input("Digite o número de linhas: "))
num_colunas = int(input("Digite o número de colunas: "))
for i in range(num_linhas):
    for j in range(num_colunas):
        if i ==0 or i==num_linhas-1 or j==0 or j ==num_colunas-1:
            print("*", end = "")
        else:
            print(" ", end="")
    print()