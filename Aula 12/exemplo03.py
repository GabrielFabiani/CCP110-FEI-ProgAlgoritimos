contatos = open("contatos.txt", "w")
while True:
    nome = input("Digite seu nome: ")
    telefone = input("Digite seu telefone: ")
    if nome == "" or telefone =="":
        break
    with open("contatos.txt", "a") as contatos:
        contatos.write(f"{nome}, {telefone}\n")

with open("contatos.txt", "r") as contatos:
    for linha in contatos:
        nome, telefone = linha.strip().split(",")
        print(f"Nome: {nome} - Telefone {telefone}")