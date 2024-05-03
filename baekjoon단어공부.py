a = input()
a = a.upper()
for i in range(len(a)):
    if len(a[i]) == 0:
        print(a[i])
    elif :

    else:
        print(max(a))
        break


a = list(input().upper())
a_set = list(set(a))
a_count = [ a.count(i)for i in a_set]

if a_count.count(max(a_count)) != 1:
    print('?')
else:
    idx = a_count.index(max(a_count))
    print(a_set[idx])