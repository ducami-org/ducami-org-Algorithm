# n = int(input())
# cnt = 0
# cnt_2 = 1
# for i in range(n):
#     a = list(input())
#     sum = 0
#     for j in a:
#         if j == 'O':
#             cnt += 1 
#             cnt_2 += cnt
#         else:
#             cnt=0
#             cnt_2 = 0
#         sum+=cnt_2
#     print(sum)

n = int(input())
cnt = 0
cnt_2 = 0
for i in range(n):
    a = list(input())
    sum = 0
    cnt = 0
    cnt_2 = 0
    for j in a:
        if j == 'O':
            cnt += 1
            cnt_2 += cnt
        else:
            cnt = 0
            cnt_2 = 0
        sum+=cnt
    print(sum)