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
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
if a > b and a>c:
    print(f"O maior valor é A: {a}")
    if b > c:
        print (a,b,c)
    elif c > b:
        print (a,c,b)
elif b > a and b >c:
    print(f"O maior valor é B: {b}")
    if a > c:
        print(b,a,c)
    elif c > a:
        print (b,c,a)
elif c > a and c >b:
    print(f"O maior valor é C: {c}")
    if a > b:
        print(c,a,b)
    elif b > a:
        print(c,b,a)
else: print("Os números são iguais")