#문자열 반복
n = int(input())
for i in range(n):
    b = []
    a,b = input().split()
    a = int(a)
    b = list(str(b))
    for j in range(len(b)):
        print(b[j]*a,end='')
    print()