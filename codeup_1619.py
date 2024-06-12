def sum(a):
    num = 0
    for i in range(len(a)):
        num+=int(a[i])
    if int(a) % num == 0:
        return "Yes"
    else:
        return "No"
a = input()
print(sum(a))