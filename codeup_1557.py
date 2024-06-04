def yak(num):
    sum = 0
    if num == 1:
        print(1)
    elif num == 0:
        print(0)
    else:
        for i in range(1, num+1):
            if num%i == 0:
                sum+=1
        print(sum)
n = int(input())
yak(n)