a=int(input())
b= int(input())
c= int(input())
total = a*b*c
d = [0 for i in range(10)]
for i in str(total):
    d[int(i)]+=1
    
for i in range(10):
    print(d[i])