import sys
a = sys.stdin.readline()
b = list(map(int,sys.stdin.readline().rstrip().split()))
b.sort()
for i in b:
    print(i,end=" ")