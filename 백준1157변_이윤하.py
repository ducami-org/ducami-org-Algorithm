w=input().upper()
s=set(w)
l=dict()
for i in s:
    l[i]=0
for i in w:
    if i in l:
        l[i]+=1
max=0
for i in l.values():
    if max<i:
        max=i

m=[key for key, value in l.items() if max==value]

if len(m)==1:
    print(''.join(m))
else:
    print('?')