def list_num(list):
    sum = min(list)
    return sum
n = int(input())
list = list(map(int, input().split()))
print(list_num(list))