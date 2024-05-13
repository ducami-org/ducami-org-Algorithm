while True:
    x,y = map(int,input().split())
    if(x==y==0):
        break
    if(x<y):
        print(f"0 {x} / {y}")
    else:
        print(f"{x//y} {x%y} / {y}")