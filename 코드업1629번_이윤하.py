def f(n):
    sum=0
    while int(n)>=10:
        total=0
        for i in n:
            total+=int(i)

        n=str(total)

    return int(n)
n=input()
print(f(n))