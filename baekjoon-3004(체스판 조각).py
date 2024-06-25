n=int(input())
tot=0
a=0
for i in range(1,n+2):
    if i%2!=0:
        a+=1
    tot+=a
print(tot)