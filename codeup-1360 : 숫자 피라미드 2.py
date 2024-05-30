# 나의코드
# n=int(input())
# c=n
# for i in range(1,n+1):
#     for j in range(1,(n+2)-i):
#         print(c,end=" ")
#     c-=1
#     print()

# 정답
n=int(input())
for i in range(n,0,-1):
    print(f"{i}"*i)