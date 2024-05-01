a,b = map(int,input().split())
d= ((100-a)*(100-b))
print(100-a, 100-b, 100-(100-a+100-b),d, d//100, d%100)
print(100-(100-a+100-b)+d//100, d%100)