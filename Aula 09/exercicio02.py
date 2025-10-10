# Uma empresa de pesquisas precisa tabular os resultados da
# seguinte enquete feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"
# As possíveis respostas são:
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o
# resultado da enquete e informe ao final o resultado da mesma.
# O programa deverá ler os valores até ser informado o valor 0,
# que encerra a entrada dos dados. Não deverão ser aceitos
# valores além dos válidos para o programa (0 a 6). Os valores
# referentes a cada uma das opções devem ser armazenados num
# vetor. Após os dados terem sido completamente informados, o
# programa deverá calcular a percentual de cada um dos
# concorrentes e informar o vencedor da enquete. O formato da
# saída foi dado pela empresa, e é o seguinte:
# O Sistema Operacional mais votado foi o Unix, com 3500 votos,
# correspondendo a 40% dos votos.

lista = []
while True:
    voto = int(input("Vote no melhor Sistema Operacional para servidores (1-6) ou 0 para parar: "))
    if voto == 0:
        break
    if 1 <= voto <=6:
        lista.append(voto)
    else:
        print("Voto inválido, Tente novamente!")
print(lista)
contadores = [0,0,0,0,0,0]
for voto in lista:
    contadores[voto-1] +=1

print(contadores)
print(f"Windows Server: {contadores[0]}")
print(f"Unix: {contadores[1]}")
print(f"Linux: {contadores[2]}")
print(f"Netware: {contadores[3]}")
print(f"Mac OS: {contadores[4]}")
print(f"Outro: {contadores[5]}")

maior = max(contadores)
indice_maior = contadores.index(maior)
sistemas = ["Windows Server" , "Unix", "Linux", "Netware", "Mac OS", "Outro"]
print(f"O Sistema Operacional mais votado foi {sistemas[indice_maior]}, com {maior} votos")