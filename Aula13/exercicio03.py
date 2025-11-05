with open ("arquivo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)

texto_sem_pontuacao = " "
for char in conteudo:
    if char.isalnum() or char.isspace():
        texto_sem_pontuacao +=char
    
print(texto_sem_pontuacao)

lista_palavra = texto_sem_pontuacao.split()
print(lista_palavra)