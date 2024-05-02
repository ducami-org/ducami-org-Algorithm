#내 답안
a = int(input())
b = [0]*a
b = list(map(int,input().split()))
print(min(b))
#다른 답안
a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)

for i in range(1, n) :
  a = a*m+d

print(a)