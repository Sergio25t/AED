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
        break

    if palpite > numero:
        print("O número é menor.")
    elif palpite < numero:
        print("O número é maior.")
    else:
        print("Acertaste!!!")

if tentativas <= 10:
    print(f"Parabéns, ganhaste! Acertaste em {tentativas} tentativas.")
else:
    print("Desculpa, atingiste o limite de 10 tentativas.")
