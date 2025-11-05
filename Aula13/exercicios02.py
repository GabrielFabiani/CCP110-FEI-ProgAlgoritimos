string = input("Digite um texto: ")

string_nova = ""
for char in string:
    if char == " ":
        continue
    string_nova += char
    
print(string_nova.lower())
if string_nova == string_nova[::-1]:
    print(f"{string_nova} é um palíndromo")
else:
    print(f"{string} não é um palíndromo")