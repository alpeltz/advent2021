with open("input.txt") as f:
    lines = f.readlines()
    depth = 0
    horz = 0
    aim = 0
    for line in lines:
        direct, val = line.split(' ')
        if(direct == 'forward'):
            horz += int(val)
            depth += aim * int(val)
        if(direct == 'down'):
            aim += int(val)
        if(direct == 'up'):
            aim -= int(val)
    print(depth*horz)
    f.close()

