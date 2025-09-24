sexo = input("Digite M para masculino e F para feminino: ")
peso = float(input("Digite seu peso em kg: "))
def doar():
    global sexo,peso
    if sexo == "M" and peso>=60:
        print("Você é homem e está apto a doar sangue")
    elif sexo=="F" and peso>=50:
        print("Você é mulher e está apta a doar sangue")
    elif sexo == "M" and peso<60:
        print("Você é homem e não está apto a doar sangue")
    elif sexo == "M" and peso<50:
        print("Você é mulher e não está apta a doar sangue")


if sexo == "M" and peso>=60:
        print("Você é homem e está apto a doa")
elif sexo=="F" and peso>=50:
        print("Você é mulher e está apta a doar sangue")

print 

