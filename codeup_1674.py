sum = 0
a = input()
for i in range(len(a)):
    sum+=int(a[i])
if sum%7 == 4:
    print("Bad")
else:
    print("Good")