a,b=map(int,input().split())
tot=0
if a%2==0:
    tot=tot+((a/2)*10)
else:
    tot=tot+((a/2)+1)
if b%2==0:
    tot=tot+((b/2)*10)
else:
    tot=tot+((b/2)+1)

print(int(tot))