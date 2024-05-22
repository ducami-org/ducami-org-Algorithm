b = 0
while b == 0:
    a,c = map(int,input().split())
    sum_ab = a+c
    if a == 0 and c ==0:
        b += 1
    else:
        print(sum_ab)