import math

soma=0
maximo= -math.inf

for i in range(10):
    numero=float(input("insira um  numero: "))
    soma+=numero
    if numero>maximo:
       maximo=numero

media=soma/10
print(" a média é", media)

print ("o maior numero é",maximo)
    
    

