# --- Exercício 3 ---
# Escreva um programa que imprima a tabuada de um número
# digitado pelo usuário

# --- Utilizando laço de repetição while ---
num = int(input("Digite um número para ver a tabuada: ")) # Solicita ao usuário um número
i = 1 # inicializa o contador
while i <= 10: # Enquanto o contador for menor ou igual a 10
    print(f"{num} x {i} = {num * i}") # Imprime a tabuada
    i = i + 1 # Incrementa o contador
    
# --- Utilizando laço de repetição for ---
num = int(input("Digite um número para ver a tabuada: ")) # Solicita ao usuário um número
for i in range(1, 11): # Para cada número no intervalo de 1 até 10
    print(f"{num} x {i} = {num * i}") # Imprime a tabuada
    