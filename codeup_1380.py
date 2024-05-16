for i in range (1, 10):
    for j in range(2, 6):
        print(f"{j} x {i} = {'%2d' % (i*j)}\t", end='')
    print()