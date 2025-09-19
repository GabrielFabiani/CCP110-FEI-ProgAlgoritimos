# --- Exercício 9 ---
#  Faça um programa que leia um valor n, inteiro e positivo,
#  calcule e mostre a seguinte soma: S =1+1/2+1/3+1/4+...+1/n

# --- Utilizando laço de repetição while ---
n = int(input("Digite um número inteiro e positivo: ")) # Solicita ao usuário um número
i = 1 # inicializa o contador
soma = 0 # inicializa a soma
while i <= n: # Enquanto o contador for menor ou igual ao número digitado
    soma = soma + 1/i # Soma o inverso do contador
    i = i + 1 # Incrementa o contador
print(f"A soma é: {soma}") # Imprime a soma

# --- Utilizando laço de repetição for ---
n = int(input("Digite um número inteiro e positivo: ")) # Solicita ao usuário um número
soma = 0 # inicializa a soma
for i in range(1, n + 1): # Para cada número no intervalo de 1 até o número digitado
    soma = soma + 1/i # Soma o inverso do contador
print(f"A soma é: {soma}") # Imprime a soma