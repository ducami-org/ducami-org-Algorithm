import math
a = int(input())
total=0
count=0
for i in range(a):
    b,c,d = input().split()
    if(d=='A+'):
       total += int(c)*4.3
    elif(d=='A0'):
        total += int(c)*4
    elif(d=='A-'):
        total += int(c)*3.7 
    elif(d=='B+'):
       total += int(c)*3.3
    elif(d=='B0'):
        total += int(c)*3
    elif(d=='B-'):
        total += int(c)*2.7 
    elif(d=='C+'):
       total += int(c)*2.3
    elif(d=='C0'):
        total += int(c)*2
    elif(d=='C-'):
        total += int(c)*1.7 
    elif(d=='D+'):
       total += int(c)*1.3
    elif(d=='D0'):
        total += int(c)*1
    elif(d=='D-'):
        total += int(c)*0.7 
    count+=int(c)
total = total/count+0.000000001
print(f"{total:.2f}")