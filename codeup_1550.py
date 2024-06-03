def num(sum):
    if sum == 0:
        return 0
    elif sum == 1:
        return 1
    elif sum == 2:
        return 2
    else:
        for i in range(sum):
            if sum == i**2:
                return i
n = int(input())
print(num(n))