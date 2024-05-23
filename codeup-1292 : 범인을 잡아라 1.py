n=input()
tot=0
for i in range(0,10):
    tot+=int(n[i])
if tot%7==4:
    print("suspect")
else:
    print("citizen")

