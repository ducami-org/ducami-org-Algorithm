a=int(input())
m=a
b=int(input())

x = list(map(int,input().split()))

for i in range(b):
    
    m+=m*x[i]*0.01




print("%.0f"%(m-a))

if a<m:
    
    print("good")
elif a==m:
    print("same")
else:

    print("bad")