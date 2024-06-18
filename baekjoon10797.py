a = int(input())
result = 0
li = list(map(int,input().split()))
for i in li:
    if str(a) in str(i) :
        result += 1
print(result)