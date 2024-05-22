a = list(map(int,input().split()))
b = list(map(int,input().split()))
sum_a = sum(a)
sum_b = sum(b)
if sum_a > sum_b:
    print(sum_a)
elif sum_a < sum_b:
    print(sum_b)
else:
    print(sum_a)