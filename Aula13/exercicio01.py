string = input("Digite um texto: ")

string_nova = ""
for letra in string:
    if letra in "aeiouAEIOU":
        string_nova += letra.upper()
    else:
        string_nova += letra
    
print(string_nova)