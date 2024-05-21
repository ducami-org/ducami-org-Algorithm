a,b = map(int, input().split())
result = 0

for i in range(a, b+1):
    if i % 2 !=0:
        print(f'+{i}',end='')
        result += i
    else:
        print(f'-{i}',end='')
        result -= i
print(f'={result}')