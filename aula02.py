# Exercício 01
Altura = float(input("Informe a sua altura: "))
PesoI = (72.7 * Altura) - 58
print(f"Seu peso ideal é: {PesoI:.2f}")

# # Exercício 02
KM = float(input("Digite a quantidade de kilômetros rodados: "))
Dia = int(input("Digite a quantidade de dias de aluguel: "))
Total = (60 * Dia)+(KM * 0.15)
print(f"Total a pagar: {Total:.2f}")

 
# Exercício 03
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
Tempo = (dias * 86400) + (horas * 3600) + (minutos * 60) + (segundos * 1)
print(f"O tempo total foi de: {Tempo:.0f} segundos")

# Exercício 04
horast = float(input("Digite o valor da hora de trabalho:"))
ntrabalho = float(input("Digite o numero de horas trabalhadas no mes:"))
SalarioBruto = (horast * ntrabalho)
impostorenda = (SalarioBruto * 11/100)
inss = (SalarioBruto * 8/100)
sindic = (SalarioBruto * 5/100)
SalarioLiq = (SalarioBruto) - (impostorenda) - (inss) - (sindic)
print("----------------------------")
print(f"+ Salário Bruto: R$ {SalarioBruto: .2f}")
print(f"- Imposto de Renda (11%): R$ {impostorenda: .2f}")
print(f"- INSS (8%): R$ {inss: .2f}")
print(f"- Sindicato (5%): R$ {sindic: .2f}")
print("----------------------------")
print(f"= Salário Líquido: R$ {SalarioLiq: .2f}")