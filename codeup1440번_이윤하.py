n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    print(f'{i+1}: ',end='')
    arr=[]
    for j in l:
            if l[i]>j:
                arr.append('>')
            elif l[i]<j:
                arr.append('<')
            else:
            
                arr.append('=')
    del arr[i]
    for j in arr:
        print(j,end=' ')
    print()



  

 

