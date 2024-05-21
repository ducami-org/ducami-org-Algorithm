a, b = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
list = sorted(list1+list2)
for i in range(len(list)):
    print(list[i], end=' ')