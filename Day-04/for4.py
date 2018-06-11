from math import sqrt

x=int(input("x:"))
son=int(sqrt(x))

is_prime=True

for i in range(2, son+1):
    if x%i==0:
        is_prime=False

if is_prime==True:
    print("asaldir")

else:
    print("asal degildir")

