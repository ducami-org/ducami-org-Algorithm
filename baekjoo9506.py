a = 0
while a != -1:
    yaksu = []
    a = int(input())
    for i in range(1,a):
        if a%i == 0:
            yaksu.append(i)
    if sum(yaksu) == a:
        for i in range(len(yaksu)):
            if i == 0:
                print(sum(yaksu),'=',yaksu[i],'+',end=' ')
            elif i == len(yaksu)-1:
                print(yaksu[i],end=' ')
            else:
                print(yaksu[i],end=' + ')
        print()
    elif a == -1:
        break
    else:
        print(f"{a} is NOT perfect.")