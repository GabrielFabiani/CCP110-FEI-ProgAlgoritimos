# Neste exercício, você simulará 1000 lançamentos de dois dados.
# Comece escrevendo uma função que simula o lançamento de um par
# de dados de seis lados cada.
# Sua função não deve aceitar nenhum parâmetro.
# Ela retornará a somatória obtida pelos dois dados.
# Escreva um programa principal que use sua função para simular
# 1000 lançamentos de dois dados.
# Como acontece em alguns programas, você deve contar o número
# de vezes que cada somatória acontece.
# Em seguida, a função principal deve exibir uma tabela que
# resume esses resultados.
# Mostre a frequência para cada resultado como uma porcentagem
# do número total de lançamentos.
from random import randint
def lancardados():
    return randint(1,6) + randint(1,6)

print(lancardados())

lista = []
for _ in range(1000):
    lista.append(lancardados())

print(lista)

dicionario = {}
for numero in lista:
    if numero in dicionario:
        dicionario[numero] = dicionario[numero] + 1
    else:
        dicionario[numero] = 1

print()
print(dicionario)
print()
for chave, valor in dicionario.items():
    print(f"{chave} : {valor/1000:.2%}")