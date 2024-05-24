n=int(input())
name=[]
for i in range(n):
    n=input()
    name.append(n[0])

l=set()
for i in name:
    if name.count(i)>=5:
        l.add(i)

list=sorted((l))

if list:
    for i in list:
        print(i,end='')
else:
    print('PREDAJA')
        

