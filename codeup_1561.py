def sum(num, num1):
    if num > num1:
        return num
    elif num < num1:
        return num1
    else:
        return num
a, b = map(int, input().split())
print(sum(a,b))