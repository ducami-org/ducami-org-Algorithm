N = int(input())
list1 = list(input().split())
M = int(input())
list2 = list(input().split())
list3 = [0 for i in range(M)]
for i in range(N):
    for j in range(M):
        if int(list2[j]) == int(list1[i]):
            list3[j] = 1
print(*list3)
# 답은 맞음 파이썬으로 못푸는 문제