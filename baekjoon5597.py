# li = [0 for i in range(31)]
# cnt = 0
# for i in range(0,len(li)-3):
#     a = int(input())
#     if a not in li:
#         li[a-1] = a
#         if a==30:
#             li[a]=a
# for i in li:
#     cnt += 1
#     if int(i) == 0:
#         if i < 31:
#             print(cnt)

num = [i for i in range(1, 31)]

for i in range(28):
    data = int(input())
    num.remove(data)
print(min(num))
print(max(num))