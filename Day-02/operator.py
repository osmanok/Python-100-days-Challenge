a = 5
b = 10
c = 3
d = 4
e = 5
a += b  # a=a+b
a -= c  # a=a-c
a *= d  # a=a*d
a /= e  # a=a/e 
print("a = ", a)

flag1 = 3 > 2 #1
flag2 = 2 < 1 #0
flag3 = flag1 and flag2 # 1 and 0 --> 0
flag4 = flag1 or flag2  # 1 or  0 --> 1
flag5 = not flag1       # not 1   --> 0
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)        #--->1 dogru mu print true
print(flag2 is not False)   #--->0 yanlis degil mi print false
