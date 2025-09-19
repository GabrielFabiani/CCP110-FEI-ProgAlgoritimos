# --- Exercício 11 ---
# Foi feita uma pesquisa entre os habitantes de uma região.
# Foram coletados os dados de idade, sexo (M/F) e salário. Faça
# um programa que informe:
# a) a média de idade do grupo;
# b) a média de salários dos homens;
# c) quantidade de mulheres com salário abaixo de R$600,00.
# Encerre a entrada de dados quando for digitada uma idade
# negativa (os dados da idade negativa não podem entrar nos
# cálculos dos itens solicitados acima)

# --- Utilizando laço de repetição while ---
count = 0 # inicializa o contador
soma_idade = 0 # inicializa a soma das idades
soma_salario_homens = 0 # inicializa a soma dos salários dos homens
count_homens = 0 # inicializa o contador de homens
count_mulheres_baixo_salario = 0 # inicializa o contador de mulheres com

while True: # Laço infinito
    idade = int(input("Digite a idade (negativa para sair): ")) # Solicita ao usuário a idade
    if idade < 0: # Se a idade for negativa
        break # Sai do laço
    sexo = input("Digite o sexo (M/F): ") # Solicita ao usuário o sexo esperando 'M' ou 'F'
    salario = float(input("Digite o salário: ")) # Solicita ao usuário o salário
    
    soma_idade = soma_idade + idade # Soma a idade digitada
    count = count + 1 # Incrementa o contador de pessoas
    
    if sexo == 'M': # Se o sexo for masculino
        soma_salario_homens = soma_salario_homens + salario # Soma o salário dos homens
        count_homens = count_homens + 1 # Incrementa o contador de homens
    elif sexo == 'F' and salario < 600: # Se o sexo for feminino e o salário for menor que 600
        count_mulheres_baixo_salario = count_mulheres_baixo_salario + 1 # Incrementa o contador de mulheres com salário abaixo de 600
        
if count > 0: # Se o contador de pessoas for maior que 0
    media_idade = soma_idade / count # Calcula a média de idade
else: # Se o contador de pessoas for igual a 0
    media_idade = 0 # A média de idade é 0
    
if count_homens > 0: # Se o contador de homens for maior que 0
    media_salario_homens = soma_salario_homens / count_homens # Calcula a média de salários dos homens
else: # Se o contador de homens for igual a 0
    media_salario_homens = 0 # A média de salários dos homens é 0
    
print(f"Média de idade do grupo: {media_idade}") # Imprime a média de idade do grupo
print(f"Média de salários dos homens: {media_salario_homens}") # Imprime a média de salários dos homens
print(f"Quantidade de mulheres com salário abaixo de R$600,00: {count_mulheres_baixo_salario}") # Imprime a quantidade de mulheres
# com salário abaixo de 600

