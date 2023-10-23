print("planetas:")
a = """
-1 Mercury 
-2 Venus 
-3 Mars 
-4 Jupiter 
-5 Saturn 
-6 Uranus"""
print(a)
peso = float(input("insira o seu peso em Kg: "))
planeta = int(input("insira o número do planeta: "))

match planeta:
    case 1:
        peso1 = peso * 0.37
        print("O seu peso", peso, "no planeta 1 (Mercury) seria", peso1)
    case 2:
        peso2 = peso * 0.88
        print("O seu peso", peso, "no planeta 2 (Venus) seria", peso2)
    case 3:
        peso3 = peso * 0.38
        print("O seu peso", peso, "no planeta 3 (Mars) seria", peso3)
    case 4:
        peso4 = peso * 2.64
        print("O seu peso", peso, "no planeta 4 (Jupiter) seria", peso4)
    case 5:
        peso5 = peso * 1.15
        print("O seu peso", peso, "no planeta 5 (Saturn) seria", peso5)
    case 6:
        peso6 = peso * 1.17
        print("O seu peso", peso, "no planeta 6 (Uranus) seria", peso6)
    case _:
        print("Número inválido. Escolha um número de 1 a 6.")