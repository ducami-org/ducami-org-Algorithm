a=0; d = 0
for i in range(7):
    name,sin = input().split()
    if(d<int(sin)):
        a = name
        d = int(sin)
        
print(a)