a = list(map(int,input().split()))
print(min(a),end=" ")
a.remove(min(a))
print(min(a), max(a))