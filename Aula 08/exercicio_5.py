# Exercício 5
# Faça um programa que:
# ▶ Imprime uma sequência de n números em ordem inversa à da leitura
# ▶ Utilize uma lista para isso.

lista = []
lista1 = lista[:]
for i in range(5):
    n = int(input("Digite um número: "))
    lista.append(n)
print(lista)
print(lista1)

