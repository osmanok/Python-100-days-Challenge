value=float(input("degeri giriniz: "))
unit=input("cm or in: ")

if unit=='cm':
    print("value: %d convert: %d" % (value, value*2.54))
elif unit=='in':
    print("value: %d convert: %d" % (value, value/2.54))
else:
    print("dogru degeri giriniz")