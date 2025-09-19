# --- Exercício 4 ---
# Faça um programa que leia 6 números inteiro positivos do
# usuário exiba o maior o número lido;

# --- Utilizando laço de repetição while ---
count = 0 # inicializa o contador
maior = 0 # inicializa a variável maior
while count < 6: # Enquanto o contador for menor que 6
    num = int(input("Digite um número inteiro positivo: ")) # Solicita ao usuário um número
    if num > maior: # Se o número digitado for maior que o maior
        maior = num # Atualiza o maior
    count = count + 1 # Incrementa o contador
    
print(f"O maior número digitado foi: {maior}") # Imprime o maior número

# --- Utilizando laço de repetição for ---
maior = 0 # inicializa a variável maior
for count in range(6): # Para cada número no intervalo de 0 até 5
    num = int(input("Digite um número inteiro positivo: ")) # Solicita ao usuário um número
    if num > maior: # Se o número digitado for maior que o maior
        maior = num # Atualiza o maior
        
print(f"O maior número digitado foi: {maior}") # Imprime o maior número
