a = list(input())
under=0
col=0
for i in a:
    if(i=='_'):
        under+=1
    elif(i==':'):
        col+=1
        
print(len(a)+col+under*5)