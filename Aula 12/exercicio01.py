with open("pares.txt", "r") as pares, open("invertido.txt", "w") as invertido:
    linhas = pares.readlines()
    for linha in reversed(linhas):
        invertido.write(linha)
     