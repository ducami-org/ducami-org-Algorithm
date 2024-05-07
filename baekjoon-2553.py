a = int(input())
b =1
for i in range(1,a+1):
    b *= i
    
b = str(b)
i=-1
c=b[-1]
while True:
    i-=1
    if(c=='0'):
        c = b[i]
    else:
        break
print(c)