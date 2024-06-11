def sum(a, num):
    for i in range(num[0], num[1]+num[0]):
        print(a[i], end='')
a = input()
num = list(map(int, input().split()))
sum(a, num)