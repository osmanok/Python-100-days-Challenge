maas=float(input("maasiniz: "))
sigorta=float(input("sigorta: "))

diff = maas + sigorta - 3500

if diff <= 0:
	rate = 0
	deduction = 0
elif diff < 1500:
	rate = 0.03
	deduction = 0
elif diff < 4500:
	rate = 0.1
	deduction = 105
elif diff < 9000:
	rate = 0.2
	deduction = 555
elif diff < 35000:
	rate = 0.25
	deduction = 1005
elif diff < 55000:
	rate = 0.3
	deduction = 2755
elif diff < 80000:
	rate = 0.35
	deduction = 5505
else:
	rate = 0.45
	deduction = 13505

vergi=abs(diff*rate-deduction)

print("Tax: %d" % (vergi))
print("Gelir: %d" % (diff + 3500 - vergi))