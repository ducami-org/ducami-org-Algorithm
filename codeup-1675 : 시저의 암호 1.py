str_list=list(input().split())
for i in range(len(str_list)):
    for j in range(len(str_list[i])):
        c=ord(str_list[i][j])-3
        if c<97:
            c=c+26
        print(chr(c),end="")
   
    print(" ",end="")