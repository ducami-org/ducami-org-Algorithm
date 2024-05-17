n=int(input())
c=0
for i in range(1,n+1):
    if (i*i) >= n:
        c=(i-1)
        break
print(f"{n-(c*c)} {c}")