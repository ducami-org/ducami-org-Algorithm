def sum(a):
    # 0 : 바위 1: 가위 2: 보
    if a[0] == a[1]:
        print("tie")
    elif a[0] == 0 and a[1] == 1:
        print("win") 
    elif a[0] == 1 and a[1] == 2:
        print("win")
    elif a[0] == 2 and a[1] == 0:
        print("win")
    else:
        print("lose")
a = list(map(int, input().split()))
sum(a)