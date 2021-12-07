import numpy as np
with open("input.txt") as f:
    line = f.readlines()[0].strip()
    crabs = np.expand_dims(np.asarray(line.split(','), np.int32),0)
    end_pos = np.expand_dims(np.arange(np.min(crabs), np.max(crabs)+1),1)
    dist = np.abs(crabs - end_pos)
    new_fuel = dist*(dist+1)/2
    fuel = np.sum(new_fuel, axis=1)
    min_pos = np.argmin(fuel)
    print("Winning position: ", end_pos[min_pos])
    print("Total fuel: ", np.min(fuel))
    f.close()
