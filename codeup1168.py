a,b = map(int,input().split())
y = a//10000
year = 0
if b == 1 or b == 2:
    year += 1900+y
elif b==3 or b==4:
    year += 2000+y
print(2012-year+1)
