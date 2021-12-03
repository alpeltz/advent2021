import copy
with open("input.txt") as f:
    lines = f.readlines()
    bits = []
    def find_most_common(lines, idx):
        val = 0
        totalLines = 0
        for line in lines:
            line = line.strip()
           
            val += int(line[idx])
            totalLines +=1
        # if the value > totalLines/2, then the most common char was 1
        if val > totalLines / 2:
            return 1
        elif val < totalLines / 2:
            return 0
        else:
            return -1

    def find_least_common(lines, idx):
        most_com = find_most_common(lines,idx)
        if(most_com == 1):
            return 0
        if(most_com==0):
            return 1
        if(most_com==-1):
            return 0
    def remove_values(lines,idx,val):
        new_list = []
        for line in lines:
            if line[idx] == str(val):
                new_list.append(line)
        return new_list

    oxygen = copy.deepcopy(lines)
    co2 = copy.deepcopy(lines)
    i = 0
    while(len(oxygen) > 1):
        most_com = find_most_common(oxygen, i)
        if most_com == -1:
            most_com = 1
        oxygen = remove_values(oxygen, i, most_com)
        i+=1
        print("oxygen:", len(oxygen))
    i = 0
    while(len(co2) > 1):
        least_com = find_least_common(co2, i)
        co2 = remove_values(co2, i, least_com)
        i+=1
        print("co2:", len(co2))

    oxygen = int(oxygen[0].strip(),2)
    co2 = int(co2[0].strip(),2)
    print(oxygen * co2)
