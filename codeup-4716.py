train=0; max=0
for i in range(10):
    x,y = map(int,input().split())
    train+=y
    train-=x
    if(max<train):
        max = train
        
print(max)