a = int(input())
d=[]
d1=[]
for i in range(a):
    b,c = input().split()
    d.append(b)
    d1.append(int(c))
    
for i in range(2):
    max1= d1.index(max(d1)) 
    del d[max1]
    del d1[max1]
    
print(d[d1.index(max(d1))])