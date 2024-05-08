a= list(map(int, input().split()))
sum = 0
for i in range(3):
    if a[i]<=170:
        print(f"CRASH {a[i]}")
        break
    sum+=1
if sum == 3:
    print("PASS")