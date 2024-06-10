def sum(a, b):
    sum = 0
    if a>b:
        for i in range(1, a+1):
            if a % i == 0:
                if b % i == 0:
                    sum = i
    else:
        for i in range(1, b+1):
            if a % i == 0:
                if b % i == 0:
                    sum = i
    return sum
a,b = map(int, input().split())
print(sum(a, b))