a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    result = b**c
    print(int(str(result)[-1]))