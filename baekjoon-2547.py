a= int(input())
for i in range(a):
    blank = input()
    b = int(input())
    total =0
    for i in range(b):
       c= int(input())
       total +=c
    if(total%b==0):
        print('YES')
    else:
        print('NO')
    total=0