lado1=int(input("medida lado 1"))
lado2=int(input("medida lado 2"))
lado3=int(input("medida lado3"))

if lado1 == lado2 == lado3 :
    print("O triagulo é equilatro")
elif  lado1 != lado2 == lado3  or lado1 ==lado2 != lado3 or lado1 ==lado3 != lado2 :
    print("o triâgulo é isosceles")
else:
    print("o triagulo é scaline")


      