a = int(input())
count=0
for i in range(a):
    b = list(input())
    for j in range(len(b)-1):
        if(b[j]=='0' and b[j+1]=='1' or b[j+1]=='I' and b[j]=='O'):
            count+=1
            break
print(count)