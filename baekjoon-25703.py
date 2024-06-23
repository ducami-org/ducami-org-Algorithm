a = int(input())
print('int a;')
print('int *ptr = &a;')
for i in range(a-1):
    if(i==0):
        print(f"int {'*'*(i+2)}ptr{i+2} = &ptr;")
    else:
        print(f"int {'*'*(i+2)}ptr{i+2} = &ptr{i+1};")        