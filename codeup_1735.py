def hello(n):
    if n == 0:
        return 
    print("hello")
    hello(n-1)
n = int(input())
hello(n)