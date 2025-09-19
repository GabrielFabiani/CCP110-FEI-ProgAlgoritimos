# --- Exercício 6 --- 
# Escreva um programa que leia números digitados pelo usuário
# ▶ O programa deve ler os números até que o 0 (zero) seja digitado.
# ▶ Quando o 0 for digitado, o programa deve exibir:
# ⋆ a quantidade de números que foram digitados;
# ⋆ a somatória destes números;
# ⋆ e a média aritmética destes números;


# --- Utilizando laço de repetição while ---
num = int(input("Digite um número (0 para sair): ")) # Solicita ao usuário um número
count = 0 # inicializa o contador
soma = 0 # inicializa a soma
while num != 0: # Enquanto o número for diferente de 0
    soma = soma + num # Soma o número digitado
    count = count + 1 # Incrementa o contador
    num = int(input("Digite um número (0 para sair): ")) # Solicita ao usuário um número
    
if count > 0: # Se o contador for maior que 0
    media = soma / count # Calcula a média
else: # Se o contador for igual a 0
    media = 0 # A média é 0
    
print(f"Quantidade de números digitados: {count}") # Imprime a quantidade de números digitados
print(f"Somatória dos números digitados: {soma}") # Imprime a somatória dos números digitados
print(f"Média aritmética dos números digitados: {media}") # Imprime a média aritmética dos números digitados


# --- utilizando While com comando break ---
count = 0 # inicializa o contador
soma = 0 # inicializa a soma
while True: # Laço infinito
    num = int(input("Digite um número (0 para sair): ")) # Solicita ao usuário um número
    if num == 0: # Se o número for igual a 0
        break # Sai do laço
    soma = soma + num # Soma o número digitado
    count = count + 1 # Incrementa o contador
    
if count > 0: # Se o contador for maior que 0
    media = soma / count # Calcula a média
else: # Se o contador for igual a 0
    media = 0 # A média é 0
    
print(f"Quantidade de números digitados: {count}") # Imprime a quantidade de números digitados
print(f"Somatória dos números digitados: {soma}") # Imprime a som
print(f"Média aritmética dos números digitados: {media}") # Imprime a média aritmética dos números digitados