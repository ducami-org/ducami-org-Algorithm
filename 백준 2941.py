d = []
a = input()
count = 0
zz = 0
for i in range(len(a)):
    if zz == 0:
        if a[i] == "c" :
            if a[i+1] == "=" or a[i+1] == "-":
                count+=1
                zz = 1
            else:
                count+=1
        elif a[i] == "d":
            if a[i+2] == "=" and a[i+1] == "z":
                count+=1
                zz = 2
            elif  a[i+1] == "-":
                count+=1
                zz = 1
            else:
                count+=1
        elif a[i] == "l":
            if a[i+1] == "j":
                count+=1
                zz = 1
            else:
                count+=1
        elif a[i] == "n":
            if a[i+1] == "j":
                count+=1
                zz = 1
            else:
                count+=1
        elif a[i] == "s":
            if a[i+1] == "=":
                count+=1
                zz = 1
            else:
                count+=1
        elif a[i] == "z":
            if a[i+1] == "=":
                count +=1
                zz = 1
            else:
                count+=1
        else:
            count+=1
    else:
        zz-=1
print(count)