a=input()
n=a[-1]+a[-2]
print((int(n)*2)%100)
if ((int(n)*2)%100) > 50:
    print("OH MY GOD")
else:
    print("GOOD")