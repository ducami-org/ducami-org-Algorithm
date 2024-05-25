def list_num(n, list):
    sum = max(list)
    j = list.index(sum) + 1
    return j
n = int(input())
list = list(map(int, input().split()))
print(list_num(n, list))