a = int(input())
count=0
for i in range(a):
    h,a,b,k = map(float,input().split())
    if((h<=56 and a<=45 and b<=25 or h+a+b<=125) and k<=7):
        print(1)
        count+=1
    else:
        print(0)
print(count)