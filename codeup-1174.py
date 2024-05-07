a,b = map(int,input().split())
total = a*60+b
total -=30
a  = total //60
b = total %60
while a<0:
    a =23
print(a,b)