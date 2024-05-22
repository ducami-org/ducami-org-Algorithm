res = []
ori = []
b = 0
while b == 0:
    a = []
    ori = []
    res = []
    a = list(map(int,input()))
    if a[0] == 0:
        b += 1
    else:
        ori.append(a)
        for i in range(len(a),0,-1):
            res.append(a[i-1])
        if res == ori[0]:
            print('yes')
        else:
            print('no')