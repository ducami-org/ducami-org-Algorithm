#내 답안
a,b,c = map(int,input().split())
result = a+b+c
result = int(result)
print("%d %.2f"%(result,result/3))
#다른 답안
a, b, c = map(int, input().split())
avg = (a+b+c)/3
print(a+b+c)
print("%0.2f" % avg)
