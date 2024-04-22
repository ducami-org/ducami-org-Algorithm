#나의 답
a,b,c=map(int,input().split())
if a>c and a>b:
    if a<(b+c):
        print("yes")
    else:
        print("no")
elif b>c and b>a:
    if b<(a+c):
        print("yes")
    else:
        print("no")
else:
    if c<(a+b):
        print("yes")
    else:
        print("no")

# 정석
nums = list(map(int, input().split()))
nums.sort()
if nums[2] < nums[0] + nums[1] :
    print("yes")
else:
    print("no")