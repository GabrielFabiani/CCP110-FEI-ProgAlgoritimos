numero = int(input("numero positivo: "))
num_anterior = 1
soma = 1
status = "Falso"
#verificar se é positivo
while True:
    if numero>=0:
        break
    else:
        numero= int(input("numero precisa ser positivo: "))
#verifica a quantidade de digitos
for i in range (2,numero):
    num_anterior = soma + num_anterior
    soma = num_anterior - soma
    if num_anterior == numero:
        status = "Verdadeiro"
        break


if numero ==0 or numero ==1:
    status = "Verdadeiro"
print(status)
