import statistics
def is_open(c):
    return c=="(" or c=="[" or c=="{" or c=="<"

def is_close(c):
    return c==")" or c=="]" or c=="}" or c==">"

def is_valid(_open,close):
    if _open=="(":
        return close==")"
    if _open=="[":
        return close =="]"
    if _open=="{":
        return close=="}"
    if _open=="<":
        return close==">"

def is_corrupted(line):
    stack=[]
    for c in line:
        if is_open(c):
            stack.append(c)
        if is_close(c):
            _open = stack[-1]
            stack = stack[:-1]
            if not is_valid(_open,c):
                return True,c
    return False,stack

with open("input.txt") as f:
    lines = f.readlines()
    illegal=[]
    incomplete = []
    for line in lines:
        line = line.strip()
        corrupt, char = is_corrupted(line)
        if corrupt:
            illegal.append(char)
        elif len(char)!=0:
            incomplete.append(char)
    total=0
    for i in illegal:
        if i==")":
            total+=3
        if i=="]":
            total+=57
        if i=="}":
            total+=1197
        if i==">":
            total+=25137
    print(total)
    total_scores=[]
    for i in incomplete:
        score=0
        i.reverse()
        for v in i:
            score *= 5
            if v == "(":
                score += 1
            if v =="[":
                score += 2
            if v=="{":
                score+=3
            if v=="<":
                score+=4
        total_scores.append(score)
    print(statistics.median(total_scores))
