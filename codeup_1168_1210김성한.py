a,b = input().split()
if int(b)>=3:
    c = int(a[:2])+2000
    print(2012-c+1)
else:
    c = int(a[:2]) + 1900
    print(2012-c+1)