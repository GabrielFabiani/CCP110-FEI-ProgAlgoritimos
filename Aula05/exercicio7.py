# --- Exercício 7 ---
# Faça um programa para calcular a somatória de 10 números
# ▶ Os número devem ser digitados pelo usuário
# ▶ Será necessário um contador para controlar o número de
# repetições
# ▶ e um acumulador para acumular a soma dos números entre cada
# repetição

# --- Utilizando laço de repetição while ---
count = 0 # inicializa o contador
soma = 0 # inicializa a soma
while count < 10: # Enquanto o contador for menor que 10
    num = int(input("Digite um número: ")) # Solicita ao usuário um número
    soma = soma + num # Soma o número digitado
    count = count + 1 # Incrementa o contador
    
print(f"A somatória dos números digitados é: {soma}") # Imprime a somatória dos números digitados


# --- Utilizando laço de repetição for ---
soma = 0 # inicializa a soma
for count in range(10): # Para cada número no intervalo de 0 até 9
    num = int(input("Digite um número: ")) # Solicita ao usuário um número
    soma = soma + num # Soma o número digitado

print(f"A somatória dos números digitados é: {soma}") # Imprime a somatória dos números digitados