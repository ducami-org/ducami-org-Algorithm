tot=0.0
for i in range(3):
    a,b=map(float,input().split())
    tot=tot+a*b
print(f"{tot:.1f}")