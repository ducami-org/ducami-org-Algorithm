def sum(num, num1):
    if (num) > (num1):
        return (num) - (num1)
    elif (num) < (num1):
        return (num1) - (num)
    else:
        return (num1) - (num)
a, b = map(int, input().split())
print(sum(a,b))