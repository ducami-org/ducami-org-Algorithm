import sys
sys.setrecursionlimit(10**6)
arr={0:0,1:1}
def nachi(n):
   if n in arr:
      return arr[n]
   arr[n] = nachi(n-1)+nachi(n-2)
   return arr[n]

n = int(input())
print(nachi(n))