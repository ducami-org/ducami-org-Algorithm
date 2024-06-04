def f(s,e):
    if s>e:
      return
    else:
       print(s)
       f(s+1,e)
e=int(input())
f(1, e)