w=input()
for i in range(len(w)):
    if i==len(w)-1:
        pass
    elif len(w)!=3:
        print('I don\'t care.')
        break

    else:
        if w[i]=='I' and w[i+1]=='O' and w[i+2]=='I':
            print('IOI is the International Olympiad in Informatics.')
            break
        else:
            print('I don\'t care.')
            break
