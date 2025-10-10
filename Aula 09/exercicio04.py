palavra_certa = ['E','V','A','P','A','R','A','R']
chutes = ["_"] * len(palavra_certa)
print(chutes)
while chutes != palavra_certa:
    letra = input("Digite uma letra: ")
    if letra in chutes:
        print("Você já chutou essa letra. Tente Outra")
        continue
    for indice, elemento in enumerate(palavra_certa):
        if elemento == letra:
            chutes[indice] = letra
    print(chutes)