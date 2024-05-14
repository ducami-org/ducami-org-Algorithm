a,b = map(int,input().split())
goal = b+1
time = a
for i in range(a,90):
    time+=5
    if time < 90:
        goal+=1
    else:
        break
print(goal)
