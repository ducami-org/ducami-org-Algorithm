# sum = 0
# sum_max = 0
# for i in range(10):
#     a,b = map(int,input().split())
#     if sum > a:
#         sum -= a
#         sum += b
#     if i == 9:
#         break
#     if sum > sum_max:
#         sum_max = sum
# print(sum_max)
sum = 0
max_sum = 0
for i in range(10):
    a,b = map(int,input().split())
    sum -= a
    sum+= b
    if i == 9:
        break
    if sum > max_sum:
        max_sum = sum
print(max_sum)