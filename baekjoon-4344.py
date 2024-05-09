a =int(input())
for i in range(a):
    count =0
    b = list(map(int,input().split()))
    b.remove(b[0])
    avg = sum(b)/len(b)
    for j in b:
        if(j>avg):
            count+=1
    print(f"{count/len(b)*100:.3f}%")
    