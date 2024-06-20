q = list(map(int, input().split()))
q.sort()
a = q[0]
b = q[1]
c = q[2]
if a == b and b == c and a == c:
    print(10000+a*1000)
elif a == b and b!= c and a!=c:
    print(1000+a*100)
elif a != b and b == c and c!=a:
    print(1000+b*100)
elif a == c and a != b and b!=c:
    print(1000+c*100)
else:
    print(c*100)