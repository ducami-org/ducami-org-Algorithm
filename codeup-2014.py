for i in range(1,10):
    for j in range(10):
        for k in range(10):
            if((100*i+10*j+k)-(10*i+j)==10*k+k ):
                print(f"{i}{j}{k}-{i}{j}={k}{k}")