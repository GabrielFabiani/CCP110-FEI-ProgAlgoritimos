# --- Exercício 2 ---
# Faça um programa que imprima os números de 1 a 50 de 1 em 1 e
# de 52 a 100 de 2 em 2;

# --- Utilizando laço de repetição while ---
i = 1 # inicializa o contador
while i <= 50: # Enquanto o contador for menor ou igual a 50
    print(i) # Imprime o número
    i = i + 1 # Incrementa o contador de 1 em 1
i = 52 # inicializa o contador
while i <= 100: # Enquanto o contador for menor ou igual a 100
    print(i) # Imprime o número
    i = i + 2 # Incrementa o contador de 2 em 2
    
    
# --- Utilizando laço de repetição for ---
for i in range(1, 51): # Para cada número no intervalo de 1 até 50
    print(i) # Imprime o número
for i in range(52, 101, 2): # Para cada número no intervalo de 52 até 100 de 2 em 2
    print(i) # Imprime o número