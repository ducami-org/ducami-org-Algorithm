n = int(input())

for i in range(n):
	for j in range(n-i-1):
		print(' ',end='')	
	print('*',end='')
	for j in range(i*2):
		print(' ',end='')
	print('*',end='')
	print()
	
for i in range(n,0,-1):
	for j in range(n-i):
		print(' ',end='')
	print('*',end='')
	for j in range(i*2-2):
		print(' ',end='')
	print('*',end='')
	print()