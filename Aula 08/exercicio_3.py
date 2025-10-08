# # Exercício 3
# # Faça um programa que:
# # ▶ Peça 10 números reais do usuário.
# # ▶ Armazene-os em uma lista e diga qual o índice do maior e seu valor

lista = []
for i in range(10):
    n = int(input("Digite um número: "))
    lista.append(n)
print(lista)

maior = lista[0]
indice_maior = 0

for indice in range(len(lista)):
    if lista[indice] > maior:
        maior = lista[indice]
        indice_maior = indice
print(f"O maior valor é {maior} no indice {indice_maior}")