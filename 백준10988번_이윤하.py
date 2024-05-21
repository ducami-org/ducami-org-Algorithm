w=input()
r=list((reversed(w)))
if w==''.join(r):
    print(1)
else:
    print(0)