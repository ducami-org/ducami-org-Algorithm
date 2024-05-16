# a = list(map(int,input().split()))
# b = True
# for i in range(len(a)):
#     if i == 0:
#         b = False
#     elif a[i] < 100:
#         print(0,end='')
#         if a[i] > 0 and i != 1 and a[i] < 10:
#             print(0,end='')
#     print(a[i],end='')
a = list(map(int,input().split()))
for i in range(len(a)):
    if i == 0:
        print(a[i],end='')
    elif i == 1:
        if a[i] > 10:
            print(a[i],end='')
        else:
            print(0,end='')
            print(a[i],end='')
    elif i == 2:
        if a[i] > 100:
            print(a[i],end='')
        elif a[i] > 10:
            print(0,end='')
            print(a[i])
        else:
            print(0,end='')
            print(0,end='')
            print(a[i],end='')
            
