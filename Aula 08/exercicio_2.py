# Exercício 2
# Faça um programa que:
# ▶ Mostre o menor valor dentro da lista T = [11, 7, 2, 4]

t = [11,7,2,4]
menor = t[0]

for elemento in t:
    if elemento < menor:
        menor = elemento
print(menor)
