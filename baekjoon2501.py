# n,k = map(int,input().split())
# li = []
# min_n = 0
# for i in range(0,n+1):
#     if i != 0:
#         if n%i==0:
#             li.append(i)
# print(li)
# if k == 1:
#     print(li[k-1])
# else:
#     print(li[k-1])

l = []
a, b = map(int, input().split())
for i in range(1, a+1):
    if a % i == 0:
        l.append(i)
if len(l) < b:
        print("0")
else:
     print(l[b-1])