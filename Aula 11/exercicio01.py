# Escreva uma função chamada procuraChave que encontre todas as
# chaves, em um dicionário, que estão associadas a um valor
# específico.
# A função receberá o dicionário e o valor a procurar como seus
# únicos parâmetros.
# A função retornará uma lista (possivelmente vazia) de chaves
# associadas ao valor fornecido.
# Faça um programa principal que mostra o funcionamento da
# função.
# Seu programa principal deve criar um dicionário e mostrar que
# a função procuraChave funciona corretamente quando retorna
# várias chaves, uma única chave ou nenhuma chave.


dicionario = {
    'alpha': 1,
    'bravo': 2,
    'charlie': 1,
    'delta': 3,
    'echo': 1

}


print(dicionario)

def procuraChave(dicionario,chaveProcurada):
   lista = []
   for chave , valor in dicionario.items():
      if valor == chaveProcurada:
        lista.append(chave)
   return lista

print("Procurando chaves com valor 1")
print(procuraChave(dicionario, 1))

print("Procurando chaves com valor 3")
print(procuraChave(dicionario, 3))

print("Procurando chaves com valor 4")
print(procuraChave(dicionario, 4))