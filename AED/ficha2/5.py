n1= int(input("insira o numero 1: "))
n2= int(input("insira numero 2: "))
n3= int(input("insira o numero 3: "))

if n1>n2>n3:
   print(n3,n2,n1)
if n1>n3>n2:
   print(n2,n3,n1)
if n3>n2>n1:
   print(n1,n2,n3)
if n2>n3>n1:
   print(n1,n3,n2)
if n2>n1>n3:
   print(n3,n1,n2)
if n3>n1>n2:
   print(n2,n1,n3)
