def is_lowest(i,j,lines):
    val = int(lines[i][j])
    if i < len(lines)-1 and int(lines[i+1][j]) <= val:
        return False
    if i > 0 and int(lines[i-1][j]) <= val:
        return False
    # minus 2 because there is a newline
    if j < len(lines[i])-2 and int(lines[i][j+1]) <= val:
        return False
    if j > 0 and int(lines[i][j-1]) <= val:
        return False
    return True

def find_basin(i,j,lines):
    queue = [(i,j)] 
    idx = 0
    while len(queue) != idx:
        i,j = queue[idx]
        idx+=1
        if i < len(lines)-1 and int(lines[i+1][j]) != 9 and (i+1,j) not in queue:
            queue.append((i+1,j))
        if i > 0 and int(lines[i-1][j]) != 9 and (i-1,j) not in queue:
            queue.append((i-1,j))
        # minus 2 because there is a newline
        if j < len(lines[i])-2 and int(lines[i][j+1]) != 9 and (i,j+1) not in queue:
            queue.append((i,j+1))
        if j > 0 and int(lines[i][j-1]) != 9 and (i,j-1) not in queue:
            queue.append((i,j-1))
    return len(queue)

with open("input.txt") as f:
    lines = f.readlines()
    total = 0
    lowest = []
    for (i,row) in enumerate(lines):
        row = row.strip()
        for (j,col) in enumerate(row):
            if is_lowest(i,j,lines):
                lowest.append((i,j))
    top,mid,low = (0,0,0)
    for l in lowest:
        size = find_basin(l[0],l[1], lines)
        if size > top:
            low = mid
            mid = top
            top = size
        elif size > mid:
            low = mid
            mid = size
        elif size > low:
            low = size
    print(top, mid, low)
    print(top*mid*low)
