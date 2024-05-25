#baekjoon2609 최대공약수와 최소공배수
a,b = map(int,input().split())
a_y = []
b_y = []
ab_y = []
for i in range(1,a+1):
    if a%i==0:
        a_y.append(i)

for i in range(1,b+1):
    if b%i==0:
        b_y.append(i)

if len(a_y) >len(b_y):
    for i in range(len(b_y)):
        if b_y[i] in a_y:
            ab_y.append(b_y[i])

else:
     for i in range(len(a_y)):
        if a_y[i] in b_y:
            ab_y.append(a_y[i])    
            
print(max(ab_y))
print((a*b)//max(ab_y))