# --- Exercício 8 ---
# Calcular a somatória de valores digitados pelo usuário:
# ▶ Continue somando até que o número 0 (zero) seja digitado;
# ▶ Quando o 0 for digitado o resultado da somatória é exibido;

# --- Utilizando laço de repetição while ---
soma = 0 # inicializa a soma
num = int(input("Digite um número (0 para sair): ")) # Solicita ao usuário
while num != 0: # Enquanto o número for diferente de 0
    soma = soma + num # Soma o número digitado
    num = int(input("Digite um número (0 para sair): ")) # Solicita ao usuário um número
    
print(f"A somatória dos números digitados é: {soma}") # Imprime a somatória dos números digitados

# --- Utilizando laço de repetição while com comando break ---
soma = 0 # inicializa a soma
while True: # Laço infinito
    num = int(input("Digite um número (0 para sair): ")) # Solicita ao usuário um número
    if num == 0: # Se o número for igual a 0
        break # Sai do laço
    soma = soma + num # Soma o número digitado
    
print(f"A somatória dos números digitados é: {soma}") # Imprime a somatória dos números digitados
    
    