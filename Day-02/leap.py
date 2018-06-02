yil=int(input("yili giriniz"))

artikmi=(yil%4==0 and yil%100!=0 or yil%400==0)

print(artikmi)