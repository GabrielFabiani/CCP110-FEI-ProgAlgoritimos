# --- Exercício 10 ---
# Elaborar um programa que leia um conjunto de valores reais,
# correspondentes a 80 notas dos alunos de uma turma, notas
# estas que variam de 0 a 10. Calcule e mostre:
# a) A quantidade de alunos aprovados (nota >=6,0)
# b) A média das notas da turma;

# --- Utilizando laço de repetição while
count = 0 # inicializa o contador
soma = 0 # inicializa a soma
aprovados = 0 # inicializa a quantidade de aprovados
while count < 80: # Enquanto o contador for menor que 80
    nota = float(input("Digite a nota do aluno (0 a 10): ")) # Solicita ao usuário a nota do aluno
    if 0 <= nota <= 10: # Se a nota estiver entre 0 e 10
        soma = soma + nota # Soma a nota digitada
        if nota >= 6: # Se a nota for maior ou igual a 6
            aprovados = aprovados + 1 # Incrementa a quantidade de aprovados
        count = count + 1 # Incrementa o contador
    else: # Se a nota for inválida
        print("Nota inválida. Digite uma nota entre 0 e 10.") # Imprime mensagem de erro
        
media = soma / 80 # Calcula a média
print(f"Quantidade de alunos aprovados: {aprovados}") # Imprime a quantidade
print(f"Média das notas da turma: {media}") # Imprime a média

# --- Utilizando laço de repetição for ---
soma = 0 # inicializa a soma
aprovados = 0 # inicializa a quantidade de aprovados
for count in range(80): # Para cada número no intervalo de 0 até 79
    nota = float(input("Digite a nota do aluno (0 a 10): ")) # Solicita ao usuário a nota do aluno
    if 0 <= nota <= 10: # Se a nota estiver entre 0 e 10
        soma = soma + nota # Soma a nota digitada
        if nota >= 6: # Se a nota for maior ou igual a 6
            aprovados = aprovados + 1 # Incrementa a quantidade de aprovados
    else: # Se a nota for inválida
        print("Nota inválida. Digite uma nota entre 0 e 10.") # Imprime mensagem de erro
        
media = soma / 80 # Calcula a média
print(f"Quantidade de alunos aprovados: {aprovados}") # Imprime a quantidade
print(f"Média das notas da turma: {media}") # Imprime a médiaria dos números digitados