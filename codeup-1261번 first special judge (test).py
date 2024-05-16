a = map(int, input().split())
a = list(a)
b = 0
for i in a:
    if i%5==0:
        print(i)
        break
    else:
        b+=1
    if b == len(a):
        print(0)