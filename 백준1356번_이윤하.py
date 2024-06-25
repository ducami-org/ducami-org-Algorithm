def mul(s):
    res=1
    for i in s:
        res*=int(i)
    return res

n=input()

c=False
for i in range(1,len(n)):
    s1=n[:i]
    s2=n[i:]
    res1=mul(s1)
    res2=mul(s2)
    if res1==res2:
        c=True
        break

if c==True:
    print('YES')
else:
    print('NO')
