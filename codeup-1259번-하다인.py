a=int(input())
b=[]
for i in range(1,a+1,1):
    if i%2==0:
        b.append(i)
print(sum(b))
