a,b = map(float,input().split())
while True:
    print(f"{a:.2f}",end=" ")
    a+=0.01
    if(a>b):
        break