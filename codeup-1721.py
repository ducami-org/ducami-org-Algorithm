import math
x,y = map(int,input().split())
x2,y2 = map(int,input().split())
print(f"{(math.sqrt(((x-x2)**2)+((y-y2)**2))):.2f}")