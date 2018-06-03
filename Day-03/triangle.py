import math as m

a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))

if a+b>c and a+c>b and b+c>a:
    print("cevre: %f" % (a+b+c))
    p=(a+b+c)/2
    area=m.sqrt(p*(p-a)*(p-b)*(p-c))
    print("alan : %f" % (area))

else:
    print("ucgen degildir")
