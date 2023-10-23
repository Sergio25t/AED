import random

numero = random.randint(1, 50)
tentativas = 1

palpite = int(input("Insira o seu palpite: "))

if palpite > numero:
    print("O número é menor.")
elif palpite < numero:
    print("O número é maior.")

while numero != palpite:
    palpite = int(input("Insira o seu palpite: "))
    tentativas += 1

    if tentativas == 11:
        print("Desculpa, atingiste o limite de 10 tentativas.")
        break

    if palpite > numero:
        print("O número é menor.")
    elif palpite < numero:
        print("O número é maior.")
    else:
        print("Acertaste!!!")
        print("acertas-te em", tentativas,"tentativas")
        recomeçar = input("Deseja recomeçar? (S/N): ")
        if recomeçar == "S":
            numero = random.randint(1, 50)
            tentativas = 0
            continue
        elif recomeçar == "N":
            break
        






    








      






