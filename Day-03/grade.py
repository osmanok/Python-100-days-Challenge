#100-90--->A
#90-70 --->B
#70-50 --->C
#50-20 --->D
#20-0  --->F

grade=int(input("notu giriniz:"))

if grade >= 90:
    print("A")
elif grade >= 70:
    print("B")
elif grade >= 50:
    print("C")
elif grade >= 20:
    print("D")
elif grade >= 0:
    print("F")
elif grade<0 or grade>100:
    print("dogru degeri giriniz") 