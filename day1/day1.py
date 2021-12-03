import math
with open('input.txt') as f:
    lines = f.readlines()
    prev_num = int(lines[0]) + int(lines[1])+ int(lines[2])
    total = 0
    for i in range(3,len(lines)):
        num = prev_num - int(lines[i-3]) + int(lines[i])
        if num > prev_num:
            total=total+1
        prev_num = num
    print("Total:",total)

    f.close()



