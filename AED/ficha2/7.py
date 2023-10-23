print("planetas:")
a = """
-1 Mercury 
-2 Venus 
-3 Mars 
-4 Jupiter 
-5 Saturn 
-6 Uranus"""
print(a)
peso=float(input("insira o seu peso e Kg: "))
planeta=int(input("insira o numero do planeta: "))

if planeta ==1:
   peso1 = (peso*0.37)
   print("o teu peso", peso , "no planeta 1 seria" ,peso1  )
elif planeta ==2:
   peso2 = (peso*0.88)
   print("o teu peso", peso ," no planeta 2 seria" ,peso2  )
elif planeta ==3:
   peso3 = (peso*0.38)
   print("o teu peso", peso ," no planeta 3 seria" ,peso3  )
elif planeta ==4:
   peso4 = (peso*2.64)
   print("o teu peso", peso ," no planeta 4 seria" ,peso4  )
elif planeta ==5:
   peso5 = (peso*1.15)
   print("o teu peso", peso ," no planeta 5 seria" ,peso5 )
elif planeta== 6:
   peso6 = (peso*1.17)
   print("o teu peso", peso ," no planeta 6 seria" ,peso6  )

else:
   print("numero invalido escolher numero de 1-6")

   
