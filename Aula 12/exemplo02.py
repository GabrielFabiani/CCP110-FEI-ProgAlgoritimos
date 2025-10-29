# # Pares divisiveis por 4
with open("pares.txt", "r") as pares, open("multiplos.txt", "w") as multiplos:
   for linha in pares.readlines():
      valor = int(linha.strip())
      if valor % 4 == 0:
         multiplos.write(linha)
