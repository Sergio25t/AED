import math

soma=0
maximo= -math.inf
numero=int(input("insira o numero de numeros quer ler: "))

for i in range(numero):
    numero2=float(input("insira um  numero: "))
    soma+=numero2
    if numero2>maximo:
       maximo=numero2

media=soma/ numero
print(" a média é", media)

print ("o maior numero é",maximo)
    