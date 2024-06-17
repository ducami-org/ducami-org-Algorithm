a,b,c = map(int,input().split(':'))
d,e,f = map(int,input().split(':'))
d -=a
e -=b
f -=c

if(f<0):
    e-=1
    f+=60
if(e<0):
    d-=1
    e+=60
if(d<0):   
    d +=24
    
if(d==e==f):
    print(f"24:00:00")
elif(d<=9 and e<=9 and f<=9):
    print(f"0{d}:0{e}:0{f}")
elif(d<=9 and e<=9):
     print(f"0{d}:0{e}:{f}")
elif(e<=9 and f<=9):
     print(f"{d}:0{e}:0{f}")
elif(d<=9 and f<=9):
     print(f"0{d}:{e}:0{f}")
elif(d<=9):
     print(f"0{d}:{e}:{f}")
elif(e<=9):
     print(f"{d}:0{e}:{f}")
elif(f<=9):
     print(f"{d}:{e}:0{f}")
else:
     print(f"{d}:{e}:{f}")
     