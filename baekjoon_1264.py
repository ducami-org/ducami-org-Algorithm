a = []
c = 0
while True:
    b = input()
    if b == "#":
        for i in range(len(a)):
            c = 0
            for j in range(len(a[i])):
                if a[i][j] == "a" or a[i][j] == "A" or a[i][j] == "e"or a[i][j] == "E" or a[i][j] == "i" or a[i][j] == "I" or a[i][j] == "o" or a[i][j] == "O" or a[i][j] == "u"or a[i][j] == "U":
                    c+=1
            print(c)
        break
    else:
        a.append(b)