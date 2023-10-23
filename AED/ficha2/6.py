genero=(str(input("insira o seu genero(M/F): ")))
idade=float(input("insira a sua idade: "))

if genero=="M":
    MHR=(220-idade)
    print(MHR,"Bpms")
elif genero =="F":
    MHR2=(226-idade)
    print (MHR2,"Bpms")