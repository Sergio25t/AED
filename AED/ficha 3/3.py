import math

fatorial=1
numero=int(input("insira o seu  numero: "))

for i in range(1,numero+1):
     fatorial=fatorial*i

print("fatorial de", numero,"é",fatorial)