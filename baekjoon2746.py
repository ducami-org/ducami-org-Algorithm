n = int(input())
a,b = 1,1
for i in range(1,n):
    a,b = b,a+b
if n == 0:
    print(0)
else:
    print(a)