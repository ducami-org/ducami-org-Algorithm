a = int(input())
d=[]
for i in range(a):
    b = int(input())
    if(b==0):
        del d[-1]
    else:
        d.append(b)
print(sum(d))