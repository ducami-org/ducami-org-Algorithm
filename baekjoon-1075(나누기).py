n=(int((input()))//100)*100
m=int(input())
tot=0
for i in range (100):
    if n%m==0:
        tot=i
        break
    else:
        n+=1
print(f"{str(tot):>02s}")


