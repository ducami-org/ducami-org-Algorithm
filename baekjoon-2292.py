a = int(input())
b=0
c=1
while True:
    if(a<=0):
        break
    a-=c
    b+=1
    c = 6*b
    
print(b)