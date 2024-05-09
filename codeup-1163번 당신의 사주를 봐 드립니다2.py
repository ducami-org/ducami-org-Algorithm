y,m,d = map(int, input().split())

if (((y+m+d) % 1000)//100)%2 == 0 :
    print("대박")
else:
    print("그럭저럭")