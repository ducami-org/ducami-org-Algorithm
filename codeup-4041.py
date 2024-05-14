a = input()
d=[]
for i in a:
    d.append(i)
    
d.reverse()
total=0
for i in d:
    if(i=='0' and total==0):
        pass
    else:
        print(i,end="")
    total += int(i)
print()
print(total)