n,k = map(int,input().split())
sum_x = 1
li = [n for i in range(k)]
for i in range(k):
    sum_x *= li[i] 
print(sum_x)
