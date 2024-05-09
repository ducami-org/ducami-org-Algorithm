b = [0]*5
sum_b = [0]*5
for i in range(5):
    a = list(map(int,input().split()))
    b[i] = a
for i in range(5):
    sum_b[i] = sum(b[i])
print(sum_b.index(max(sum_b))+1,max(sum_b))
