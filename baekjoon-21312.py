a,b,c = map(int,input().split())
odd=[]
even=[]
total=1
if(a%2==0):
    even.append(a)
elif(a%2==1):
    odd.append(a)
if(b%2==0):
    even.append(b)
elif(b%2==1):
    odd.append(b)
if(c%2==0):
    even.append(c)
elif(c%2==1):
    odd.append(c)
    
if(len(odd)==0):
    for i in even:
        total *= i
else:
    for i in odd:
        total*=i
print(total)