# --- Exercício 1 ---
# Faça um programa que imprima os números ímpares entre 0 e um
# número digitado pelo usuário

# --- Utilizando laço de repetição while ---
num = int(input("Digite um número: ")) # Solicita ao usuário um número
i = 0 # inicializa o contador 
while i <= num: # Enquanto o contador for menor ou igual ao número digitado
    if i % 2 != 0: # Se o número for ímpar o resto da divisão de i por 2 é diferente de 0
        print(i) # Imprime o número
    i = i + 1 # Incrementa o contador
    
# --- Utilizando laço de repetição for ---
num = int(input("Digite um número: ")) # Solicita ao usuário um número
for i in range(0, num): # Para cada número no intervalo de 0 até o número digitado
    if i % 2 != 0: # Se o número for ímpar o resto da divisão de i por 2 é diferente de 0
        print(i) # Imprime o número
