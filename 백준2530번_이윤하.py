h,m,s=map(int,input().split())
d=int(input())

t=s+m*60+h*3600+d

a=t//3600%24
b=t%3600//60
c=t%3600%60

print(a,b,c)



