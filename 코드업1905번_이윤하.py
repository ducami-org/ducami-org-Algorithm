import sys
sys.setrecursionlimit(1000000)

def s(n):
    if n<=1:
        return 1
        
    else:
        result=s(n-1)+n
        return result
        
print(s(int(input())))
