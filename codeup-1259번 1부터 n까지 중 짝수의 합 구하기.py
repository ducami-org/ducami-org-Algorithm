n = int(input())
hap = 0

for i in range(n+1):
    if i % 2 == 0:
        hap += i
print(hap)