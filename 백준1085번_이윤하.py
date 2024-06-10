x,y,w,h=map(int,input().split())
l=[[0]*w for i in range(h)]
d=[w-x,h-y,w-(w-x),h-(h-y)]
print(min(d))
