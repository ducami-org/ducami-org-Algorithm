n=int(input())
c_s=-1

for i in range((n*2)-1):
    if i>int((n*2)/2-1):
        c_s-=2
        print(" "*(i-int((n*2)/2-1)),end="")
        print("*"*c_s,end="")
        print()
    else:
        c_s+=2
        print(" "*(int(((n*2)/2-1)+1)-(i+1)),end="")
        print("*"*c_s,end="")
        print()
        
