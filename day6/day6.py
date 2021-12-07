import numpy as np
with open("input.txt") as f:
    lines = f.readlines()
    start = lines[0].strip().split(',')
    fish = np.zeros(9, np.int64)
    for s in start:
        fish[int(s)] +=1
    for i in range(256):
        if i %10 == 0:
            print("Progress: ", i/256) 
        # add new fish for any fish that have a val of 0
        fish = np.insert(fish, 9, fish[0])
        # set values of 0 to 6
        # this is indexing on 7 instead of 6 because we
        # delete the first index later
        fish[7] += fish[0]
        fish = np.delete(fish,0)
    print(np.sum(fish))    
