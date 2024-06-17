alpa=[0]*6
num=[0]*6
m = input()
m1,m2=m[0],m[1]
check=0
alpa[ord(m1)-65]+=1
num[int(m2)-1]+=1
k1,k2 = m1,m2
for i in range(35):
    n = input()
    n1,n2=n[0],n[1]
    alpa[ord(n1)-65]+=1
    num[int(n2)-1]+=1
    if(abs(ord(n1)-ord(k1))>=3 or abs(int(n2)-int(k2))>=3):
        check+=1
        break
    
    if(abs(ord(n1)-ord(k1))+abs(int(n2)-int(k2))!=3):
        check+=1
        break
    k1,k2=n1,n2

total = abs(ord(n1)-ord(m1))+abs(int(n2)-int(m2))
if(alpa.count(6)==6 and num.count(6)==6 and total==3 and check==0):
    print('Valid')
else:
    print('Invalid')