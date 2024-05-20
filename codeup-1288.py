a,b = map(int,input().split())
c =1; d=1; e=1
for i in range(1,a+1):
    c = c*i
for i in range(1,b+1):
    d *= i
for i in range(1,a-b+1):
    e *=i
print(c//(d*e))