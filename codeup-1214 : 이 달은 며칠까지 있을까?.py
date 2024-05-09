a,b=map(int,input().split())
di={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
if (a%400==0 or (a%4==0 and a%100!=0)) and b==2 :
    print(29)
else:    
    print(di[b])