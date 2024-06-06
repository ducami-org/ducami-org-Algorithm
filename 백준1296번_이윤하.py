w=input()
n = int(input())
li = sorted([input() for i in range(n)])

max=mi=0
for i in range(n):
    L=w.count('L')+li[i].count('L')
    O=w.count('O')+li[i].count('O')
    V=w.count('V')+li[i].count('V')
    E=w.count('E')+li[i].count('E')
    p=((L+O)*(L+V)*(L+E)*(O+E)*(E+V)*(O+V))%100
    if max<p:
        max=p
        mi=i


print(li[mi])
