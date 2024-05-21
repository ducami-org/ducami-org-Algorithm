a,b,c=map(int,input().split())
for i in range(a,90,5):
    b+=1
if c==b:
    print("same")
elif b>c:
    print("win")
else:
    print("lose")