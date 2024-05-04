max=-1000001
min=1000001
for i in range(5):
    n=int(input())
    if max<n:
        max=n
    
    if min>n:
        min=n

print(max)
print(min)