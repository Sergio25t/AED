genero=(str(input("insira o seu genero(M/F)")))
altura=(float(input("isira a sua altura")))
h=altura
if genero=="M":
    idealwheight1= (h-100)-(h-150)/4
    print(idealwheight1)
elif  genero =="F":
    idealwheight2= (h-100)-(h-150)/2
    print(idealwheight2)

   