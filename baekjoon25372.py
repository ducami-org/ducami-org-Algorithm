a = int(input())
chr = [0]*a
for i in range(0,a):
    chr[i] = input()
for i in range(a):
    if 6<= len(chr[i]) <=9:
        print('yes')
    else:
        print('no')