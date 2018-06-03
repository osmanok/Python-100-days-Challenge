"""
	    3x - 5	(x > 1)
f(x) =  x + 2	(-1 <= x <= 1)
		5x + 3	(x < -1)
"""

x=int(input("x'i giriniz"))

if x>1:
    sonuc=(3*x)-5
elif -1<=x and 1>=x:
    sonuc=x+2
else:
    sonuc=(5*x)+3

print(sonuc)
