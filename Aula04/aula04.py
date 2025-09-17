# a = int(input("Lado a: "))
# b = int(input("Lado b: "))
# c = int(input("Lado c: "))
# if (a < b + c) and (b < a + c) and (c < a + b):
#      if (a == b) and ( b == c):
#        print("Triângulo equilátero")
#      else:
#          if (a == b) or (a == c) or (b == c):
#           print("Triângulo is isóceles")
#          else:
#           print("Triângulo escaleno")
# else:
#  print("Não é Triângulo")

# Exercício 01
# preco = float(input("Digite o preço do produto: "))
# cd = int(input("Digite o código de origem do produto: "))
# if cd ==1:
#     procedencia = "Sul"
# elif cd ==2:
#     procedencia = "Norte"
# elif cd ==3:
#     procedencia = "Leste "
# elif cd ==4:
#     procedencia = "Oeste"
# elif cd ==5 or cd==6:
#     procedencia = "Nordeste"
# elif cd ==7 or cd==8 or cd==9:
#     procedencia = "Sudeste"    
# elif cd >=10 and cd <=20:
#     procedencia = "Centro-Oeste"
# elif cd >=25 and cd <=30:
#     procedencia = "Nordeste"
# else:
#     procedencia = "Importado"

# print(f"O produto custa {preco:.2f} e é originário do(a): {procedencia}")

#Exercício 02
# a = int(input("Digite o primeiro número: "))
# b = int(input("Digite o segundo número: "))
# c = int(input("Digite o terceiro número: "))
# if a > b and a>c:
#     print(f"O maior valor é A: {a}")
#     if b > c:
#         print (a,b,c)
#     elif c > b:
#         print (a,c,b)
# elif b > a and b >c:
#     print(f"O maior valor é B: {b}")
#     if a > c:
#         print(b,a,c)
#     elif c > a:
#         print (b,c,a)
# elif c > a and c >b:
#     print(f"O maior valor é C: {c}")
#     if a > b:
#         print(c,a,b)
#     elif b > a:
#         print(c,b,a)
# else: print("Os números são iguais")
# else: print("Os números são iguais")

# Exercício 03
# sexo = input("Digite seu sexo, M ou F: ")
# altura = float(input("Digite sua altura: "))

# if sexo == "M" or sexo == "m":
#     peso_i = (72.7 * altura)-58
#     print(f"O seu peso ideal é: {peso_i:.2f}")

# elif sexo=="F" or sexo=="f":
#     peso_i=(62.1 * altura)-44.7
#     print(f"O seu peso ideal é: {peso_i:.2f}")

# else:
#     print("Digite um sexo válido")

# Exercício 04
# ano_nasc = int(input("Digite seu ano de nascimento: "))
# idade = 2025 - ano_nasc
# if idade >=16 and idade<18:
#     print(f"Sua idade é {idade} anos, e você já tem idade para votar")

# elif idade>=16 or idade>=18:
#     print(f"Sua idade é {idade} anos, e você já tem idade para votar e tirar a Carteira de Habilitação")

# else:
#     print(f"Você tem {idade} anos e ainda não pode votar nem tirar sua Carteira de habilitação")

#Exercício 05
# codigo = int(input("Digite o código do produto: "))
# if codigo==1:
#     print("Alimento não perecível")
# elif codigo==2 or codigo==3 or codigo==4:
#     print("Alimento perecível")
# elif codigo==5 or codigo==6:
#     print("Vestuário")
# elif codigo==7:
#     print("Higiene pessoal")
# elif codigo>=8 and codigo<=15:
#     print("Limpeza e utensílios domésticos")
# else:
#     print("Inválido")

