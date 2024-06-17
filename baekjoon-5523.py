import sys

input = sys.stdin.readline
x1=0
y1=0
for i in range(int(input())):
    x,y = map(int,input().split())
    if(x>y):
        x1+=1
    elif(x<y):
        y1+=1
print(x1,y1)