peso= float(input("insira o seu peso em Kg"))
altura= float(input("insira a sua altura em metros"))
IMCresultado= peso/(altura**2)
print("IMC", IMCresultado)

if IMCresultado < 18.5:
   print ("under wheght")
elif IMCresultado < 25:
   print(" Healthy")
elif IMCresultado < 30:
   print ("overwheight")
elif IMCresultado  <35:
   print("obise grade 1")
elif IMCresultado <40:
   print("obisity grade 2")
elif IMCresultado >= 40:
   print("obisity level 3")



