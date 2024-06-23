a = list(map(int,input().split()))
a.sort()
b = input()
for i in b:
    print(a[ord(i)-65],end=" ")