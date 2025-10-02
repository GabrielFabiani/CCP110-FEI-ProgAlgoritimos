# Exercício 01
# for i in range(5):
#     if i ==4:
#         continue
#     else:
#         print(i, end="")
# else:
#     print("Aqui", end= " ")   

# Exercício 02
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i ==3:
#         break
# else:
#     print(0)

# Exercício 03
# quantidade = int(input("Entre com a quantidade de números que serão digitados: "))
# maior = None  
# for i in range(1, quantidade + 1):
#     numero = int(input(f"número {i}: "))
#     if maior is None or numero > maior:
#         maior = numero

# print(f"Maior número digitado: {maior}")

# Exercício 04
# n = int(input("Digite o número desejado: "))
# if n < 0:
#     print("Digite um número inteiro e positivo.")
# else:
#     e = 1.0
#     for i in range(1, n + 1):
#         e += 1 / i

#     print(f"{e:.3f}")

# Exercício 05
# Lê a quantidade de casos de teste
# N = int(input())

# # Inicializa os contadores
# total = 0
# coelhos = 0
# ratos = 0
# sapos = 0

# Para cada experimento
# N = int(input())
# total = 0
# coelhos = 0
# ratos = 0
# sapos = 0
# for _ in range(N):
#     quantidade = int(input())
#     tipo = input().strip().upper()  # Remove espaços e transforma em maiúsculo

#     total += quantidade

#     if tipo == 'C':
#         coelhos += quantidade
#     elif tipo == 'R':
#         ratos += quantidade
#     elif tipo == 'S':
#         sapos += quantidade

# # Calcula percentuais
# percentual_coelhos = (coelhos / total) * 100
# percentual_ratos = (ratos / total) * 100
# percentual_sapos = (sapos / total) * 100

# # Exibe os resultados
# print(f"Total: {total} cobaias")
# print(f"Total de coelhos: {coelhos}")
# print(f"Total de ratos: {ratos}")
# print(f"Total de sapos: {sapos}")
# print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
# print(f"Percentual de ratos: {percentual_ratos:.2f} %")
# print(f"Percentual de sapos: {percentual_sapos:.2f} %")

# Exercício 06
# ano_desejado = int(input("Digite o ano desejado: "))

# salario = 5000.00
# aumento = 0.015

# ano = 2006  # Primeiro aumento foi em 2006

# # Aplica o aumento de 2006
# salario += salario * aumento

# # A partir de 2007, os aumentos dobram
# while ano < ano_desejado:
#     aumento *= 2
#     salario += salario * aumento
#     ano += 1

# # Agora formatamos corretamente:
# print(f"Salário de {ano_desejado}: R$ {salario:.2f}")
