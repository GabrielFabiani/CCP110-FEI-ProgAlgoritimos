# Exercício 01
for i in range(10):
    n = int(input("Digite a qtde de números a serem testados: "))
    num_primo = 0
    for i in range(n):
        num = int(input("Digite um número inteiro: "))
        eh_primo = True


        for i in range(2,num):
            if num % i==0:
                eh_primo = False
                break

        if eh_primo and num > 1:
            num_primo = num_primo+1

    print(f"Foram digitados {num_primo} números primos entre {n} números")