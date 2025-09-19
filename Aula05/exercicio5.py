# --- Exercício 5 ---
# Faça um programa que solicita um número entre 0 e 10
# ▶ Mostre uma mensagem de erro caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.
# ▶ Quando o valor for válido dê a mensagem “número aceito”.
# ▶ Dica: você pode utilizar operadores lógicos (and ou or) na
# condição do while também

# --- Utilizando laço de repetição while ---
num = int(input("Digite um número entre 0 e 10: ")) # Solicita ao usuário um número
while num < 0 or num > 10: # Enquanto o número for menor que 0 ou maior que 10
    print("Número inválido. Tente novamente.") # Imprime mensagem de erro
    num = int(input("Digite um número entre 0 e 10: ")) # Solicita ao usuário um número
print("Número aceito.") # Imprime mensagem de número aceito

# --- Utilizando laço de repetição for ---
# Não é possível utilizar laço de repetição for para este exercício
# pois não sabemos quantas vezes o usuário irá errar
