n = int(input())
f = n
sum_ = 1
for i in range(n):
    sum_ *= f
    f -= 1
print(sum_)