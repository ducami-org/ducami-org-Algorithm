def f(n):
    if n>=90:
        return 'A'
    elif n<90 and n>=80:
        return 'B'
    elif n<80 and n>=70:
        return 'C'
    elif n<70 and n>=60:
        return 'D'
    else:
        return 'F'
n=int(input())
print(f(n))