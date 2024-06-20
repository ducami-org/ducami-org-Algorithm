a = input()
count=0
for i in range(len(a)):
    if a[i] == "c":
        if a[i:+i+2] == "c=":
            count+=1
        elif a[i:+i+2] == "c-":
            count+=1
    elif a[i] == "d":
        if a[i:i+3] == "dz=":
            count+=1
        elif a[i:i+2] == "d-":
            count+=1
    elif a[i] == "l":
        if a[i:i+2] == "lj":
            count+=1
    elif a[i] == "n":
        if a[i:i+2] == "nj":
            count+=1
    elif a[i] == "s":
        if a[i:i+2] == "s=":
            count+=1
    elif a[i]== "z":
        if a[i:i+2] == "z=":
            count+=1
print(count)
print(a[0:2])