a = map(int,input().split())
total =0
for i in a:
    total += i*i
print(total%10)