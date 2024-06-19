N = int(input())
K = 1
cnt = 0

while True:
    N -= K
    cnt += 1
    K += 1
    if K > N and N !=0 :
        K = 1
    if N <= 0:
        break
print(cnt)