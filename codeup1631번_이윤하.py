a = input().split('x')

if a[1][0] == '+':
    # 왼쪽과 오른쪽을 분할합니다.
    l = int(a[1].split('=')[1])
    r = int(a[1].split('+')[1].split('=')[0])
    
    sum = (l - r)/int(a[0])

if a[1][0] == '-':
    # 왼쪽과 오른쪽을 분할합니다.
    l = int(a[1].split('=')[1])
    r = int(a[1].split('-')[1].split('=')[0])
    # l에서 r을 빼고 결과를 출력합니다.
    sum = (l + r)/int(a[0])
   

    
print(f'{sum:.2f}')

    