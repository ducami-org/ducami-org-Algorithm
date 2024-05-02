a,b = map(int,input().split())
a = 90-a
if(a%5==0):
    print(b+(a//5))
else:
    print(b+(a//5)+1)