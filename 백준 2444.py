a = int(input())
d = 1   
for i in range(a-1, -1, -1):
    print(" "*i, "*"*d, sep='')
    d+=2
d-=4
for i in range(1, a):
    print(" "*i, "*"*d, sep='')
    d-=2