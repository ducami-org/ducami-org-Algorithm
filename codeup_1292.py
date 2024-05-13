a = input()
a = list(a)
sum = 0
for i in range(len(a)):
    sum  = int(a[i])+sum
if sum % 7 == 4:
    print("suspect")
else:
    print("citizen")