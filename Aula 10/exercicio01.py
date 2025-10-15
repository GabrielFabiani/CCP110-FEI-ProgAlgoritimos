# Crie 3 listas:
# ▶ Inteiros: a primeira lista com 10 números inteiros gerados
# aleatoriamente
# ▶ Reais: a segunda lista com 5 números reais gerados
# aleatoriamente
# ▶ Strings: A terceira lista com 7 strings criadas por você.
# Então adicione as 3 listas a uma lista única, chamada
# completa.
# Apague todas as 3 listas originais.
# Acesse e mostre todos os elementos da lista completa.
# Use:
# from random import randint, random
# print(randint(0, 10))
# print(random() * 10)
from random import randint, random

inteiros = [randint(1,100) for i in range(10)]
print(f"Lista de Inteiros: {inteiros}")

reais = [random() * 100 for i in range(5)] 
print(f"Lista de Reais: {reais}")

strings = ['Garibaldo','Gertrudes','Camila','Cládia','Antonieta','Marcos','Josefa']
print(f"Lista de Strings: {strings}")


print("-------------------------------------")
listas = [inteiros[:],reais[:],strings[:]]

del inteiros
del reais
del strings
print(f"Lista geral: {listas}")