def sum(a):
    a = str(a)
    if a[-1] == "0":
        a = float(a)
        a = int(a)
    else:
        a = float(a)
    return abs(a)
a = float(input())
print(sum(a))