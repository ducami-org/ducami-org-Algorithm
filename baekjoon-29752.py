a = int(input())
b = list(input().split())
result=0
sum=0

for i in b:
    if(i!='0'):
        sum+=1
        result = max(result, sum)
    if(i=='0'):
        result = max(result, sum)
        sum=0
print(result)