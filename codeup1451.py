# n = int(input())
# a = []
# for i in range(n):
#     a.append(int(input()))
# a.sort()
# for i in a:
#     print(i)

def hamsu(n):
    if n == 0:
        return 0
    return n + hamsu(n-1)

n = int(input())
print(hamsu(n))