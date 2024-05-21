a = int(input())
cnt=0
total=0
for i in range(a):
    b,c,d,e = input().split()
    c = int(c)
    d = int(d)
    e = int(e)
    if(b[0]=='A'):
        cnt += (d//12) * (c//12) * (e//12)
        total += 1000
        
    else:
        total += 6000
        
print(total+ (cnt*500))
print(cnt*4000)

