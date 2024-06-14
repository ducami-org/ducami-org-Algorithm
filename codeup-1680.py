for T in range(1,10):
    for S in range(1,10):
        for O in range(10):
            if(((10*S)+O)*2==(T*100)+O*10+O):
                print(f"{S}{O}+{S}{O}={T}{O}{O}")