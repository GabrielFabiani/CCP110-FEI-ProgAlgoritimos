# Exercício 5
# Faça um programa que:
# ▶ Imprime uma sequência de n números em ordem inversa à da leitura
# ▶ Utilize uma lista para isso.

lista = []
for i in range(5):
    n = int(input("Digite um número: "))
    lista.append(n)

lista1 = lista[::-1]
print(lista)
print(lista1)

