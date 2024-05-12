a,b,c= map(int,input().split())
total =0
for i in range(1,a+1):
    total += (b*i) + (c*i*i)
print(total)