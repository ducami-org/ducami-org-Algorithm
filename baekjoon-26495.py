a = input()
count=0
for i in a:
    if(int(i)==0):
        print("0000")
        print("0  0")
        print("0  0")
        print("0  0")
        print("0000")
    elif(int(i)==1):
        print("   1")
        print("   1")
        print("   1")
        print("   1")
        print("   1")
    elif(int(i)==2):
        print("2222")
        print("   2")
        print("2222")
        print("2")
        print("2222")
    elif(int(i)==3):
        print("3333")
        print("   3")
        print("3333")
        print("   3")
        print("3333")
    elif(int(i)==4):
        print("4  4")
        print("4  4")
        print("4444")
        print("   4")
        print("   4")
    elif(int(i)==5):
        print("5555")
        print("5")
        print("5555")
        print("   5")
        print("5555")
    elif(int(i)==6):
        print("6666")
        print("6")
        print("6666")
        print("6  6")
        print("6666")
    elif(int(i)==7):
        print("7777")
        print("   7")
        print("   7")
        print("   7")
        print("   7")
    elif(int(i)==8):
        print("8888")
        print("8  8")
        print("8888")
        print("8  8")
        print("8888")
    elif(int(i)==9):
        print("9999")
        print("9  9")
        print("9999")
        print("   9")
        print("   9")
    count +=1
    if(len(a) != count):
        print()