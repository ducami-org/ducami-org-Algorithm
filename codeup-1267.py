a = int(input())
b= list(map(int,input().split()))
total = sum(b)
for i in b:
    if(i%5!=0):
        total -= i
print(total)