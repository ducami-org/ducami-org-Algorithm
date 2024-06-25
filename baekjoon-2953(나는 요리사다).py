tot=0
tot_n=0
for i in range(5):
    arr=list(map(int,input().split()))
    if tot <= sum(arr):
        tot=sum(arr)
        tot_n=i+1
print(tot_n,tot)