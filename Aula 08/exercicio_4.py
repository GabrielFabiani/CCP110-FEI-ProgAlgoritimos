# Exercício 4
# Faça um programa para criar uma lista de 10 elementos do
# usuário e aprsente:
# ▶ a soma dos elementos pares
# ▶ a soma dos elementos de índice par
lista = []
for i in range(10):
    n = int(input("Digite um número: "))
    lista.append(n)
print(lista)

somar_par = 0
soma_indice_par = 0

for indice in range(len(lista)):
    if lista[indice] % 2 ==0:
        somar_par+=lista[indice]
    if indice % 2 ==0:
        soma_indice_par +=lista[indice]
print(f"A soma dos números pares é: {somar_par}")
print(f"A soma dos elementos no índice par é: {soma_indice_par}")