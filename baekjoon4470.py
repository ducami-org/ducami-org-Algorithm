n = int(input())
b = []
for i in range(1,n+1):
    b.append(input())

for i in range(1,len(b)+1):
    print(f'{i}. {b[i-1]}')