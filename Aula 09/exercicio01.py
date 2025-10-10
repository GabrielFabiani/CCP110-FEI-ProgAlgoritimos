# Faça um programa que leia uma quantidade indeterminada de
# números positivos e conte quantos deles estão nos seguintes
# intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada
# de dados deverá terminar quando for lido um número negativo.
contadores = [0,0,0,0]
while True:
    numero = int(input("Digite um número positivo(ou negativo para parar): "))
    if numero < 0:
        break
    if 0 <= numero <=25:
        contadores[0] +=1
    if 26 <= numero <=50:
        contadores[1] +=1
    if 51 <= numero <=75:
        contadores[2] +=1
    elif 76 <= numero <=100:
        contadores[3] +=1


print(f"Números no intervalo [0-25]: {contadores[0]}")
print(f"Números no intervalo [26-50]: {contadores[1]}")
print(f"Números no intervalo [51-75]: {contadores[2]}")
print(f"Números no intervalo [76-100]: {contadores[3]}")