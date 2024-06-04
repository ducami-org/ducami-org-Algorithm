while True:
    x,y,z = map(int,input().split())
    d=[x,y,z]
    max1 = max(d)
    d.remove(max1)
    if(x==y==z==0):
        break
    else:
        if(max1>=sum(d)):
            print('Invalid')
        elif(x==y==z):
            print('Equilateral')
        elif(x==y or y==z or z==x):
            print('Isosceles')
        else:
            print('Scalene')