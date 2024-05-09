a = list(map(int,input().split()))
check=0
for i in a:
    if(i<=170):
        print(f'CRASH {i}')
        check+=1
        break
    
if(check==0):
    print('PASS')