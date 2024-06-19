time, min = map(int, input().split())
plus = int(input())
min+=plus
while True:
    if plus>=0:
        if min>=60:
            min -= 60
            plus-=60
            time+=1
            if time>=24:    
                time = 0
    else:
        print(time, min)
        break