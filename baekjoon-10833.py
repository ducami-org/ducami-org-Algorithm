a =int(input())
total =0
for i in range(a):
    x,y = map(int,input().split())
    total += y%x
print(total)