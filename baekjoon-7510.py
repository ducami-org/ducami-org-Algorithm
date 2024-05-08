a = int(input())
for i in range(a):
    x = list(map(int,input().split()))
    y = max(x)
    x.remove(y)
    if(x[0]**2+x[1]**2==y**2):
        print(f'Scenario #{i+1}:')
        print('yes')
        print()
    else:
        print(f'Scenario #{i+1}:')
        print('no')
        print()