a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
check=[0 for i in range(10)]
count =0
f = [a,b,c,d,e]
for i in f:
    check[i]+=1
    
for i in range(len(check)):
    if(check[i]%2==1):
        print(i)
        break
    
