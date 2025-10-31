# Faça um programa que gere 100 números aleatórios
# Gere números no intervalo de 0 à 20
# Mostre quantas vezes cada número apareceu
# Dica:
# Utilize um dicionário para armazenar o número como chave
# e a quantidade de vezes em que ele aparece como valor
from random import randint
lista = []
for i in range(100):
    lista.append(randint(0,20))
    
print()
print(lista)
print()

dicionario = {}
for numero in lista:
    if numero in dicionario:
        dicionario[numero] = dicionario[numero] + 1
    else:
        dicionario[numero] = 1

print()
print(dicionario)