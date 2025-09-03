# exercício 01
# a = int(input("Digite um número: "))
# b = int(input("Digite um outro número: "))

# if a > b:
#     print(f"Maior: {a} ")
# if b > a:
#    print(f"Maior: {b} ")


# # Exercício 02
# a = int(input("Digite um número: "))
# if a >=0:
#         print("O número é positivo")
# else:
#     print("O número é negativo")
    
# Exercício 03
# print("----------------------------")
# print("       Dias da semana       ")
# dias = int(input("Digite o dia da semana: "))
# if dias == 1:
#     print("O dia da semana é Domingo")
# if dias == 2:
#     print("O dia da semana é Segunda-Feira")
# if dias == 3:
#     print("O dia da semana é Terça-Feira")
# if dias == 4:
#     print("O dia da semana é Quarta-Feira")
# if dias == 5:
#     print("O dia da semana é Quinta-Feira")
# if dias == 6:
#     print("O dia da semana é Sexta-Feira")
# if dias == 7:
#     print("O dia da semana é Sábado")

#Exercício 04
# salario = float(input("Digite o valor do salario atual: "))
# if salario > 1250:
#      novo_salario = salario * 1.1
#      print("O funcionário tem direito a 10% de aumento")
#      print(f"Novo salário {novo_salario:.2f}")
# else:
#      salario <= 1250
#      novo_salario = salario * 1.15
#      print("O funcionário tem direito a 15% de aumento")
#      print(f"Novo salário {novo_salario:.2f}")

# Exercício 05
# anoatual = int(input("Digite o ano atual: "))
# anonasc = int(input("Digite o seu ano de nascimento: "))
# aniversário = anoatual - anonasc
# if aniversário >= 18:
#     print(f"Sua idade é {aniversário}, você pode tirar sua CNH ")

# Exercício 06
# print("------------------------------------------------------")
# print("               Tabela de anos dos carros              ")
# print("       Carros com menos de 3 anos de fabricação - Novo")
# print("       Carros com mais de 3 anos de fabricação - Velho")
# carro = int(input("Digite o ano do seu carro: "))
# novo = 2025 - carro
# velho = 2025 - carro
# if carro >=2022:
#     print(f"O seu carro é novo pois foi fabricado há {novo} anos atrás")
# else: 
#     carro <2022
#     print(f"O seu carro é velho pois foi fabricado há {velho} anos atrás ")

# Exercício 07
# km = int(input("Digite a quantidade de km da viagem: "))

# if km <=200:
#     curta = km * 0.50
#     print(f"Você pagará R${curta:.2f} reais pois sua viagem tem até 200km")
# else:
#     km > 200
#     longa = km * 0.45
#     print(f"Você pagará R${longa:.2f} reais pois sua viagem tem mais de 200km")

# exercício 08
# from math import ceil
# altura = float(input("digite a altura do cilindro: "))
# raio = float(input("digite o raio: ")) 

# area_base= 3.1415* (raio**2)

# perimetro= 2* 3.1415 * raio
# area_lateral= altura*perimetro

# area_total = area_lateral + area_base

# litros = area_total/3
# latas = ceil(litros/5)

# if latas == 1:
#     preco_unit=50
# if latas == 2:    
#     preco_unit=48
# if latas == 3:
#     preco_unit=46
# else:
#     preco_unit=45

# preco_total= preco_unit * latas

# print(f"Área a ser pintada: {area_total:.2f}")
# print(f"Quantidade de litros necessários: {litros:.2f}")
# print(f"Quantidade de latas: {latas:.2f}")
# print(f"Preco unitário de lata R$ {preco_unit:.2f}")
# print(f"Custo total: R${preco_total}")

