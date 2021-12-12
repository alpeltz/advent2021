from enum import Enum
from collections import Counter
class Size(Enum):
    BIG=1
    SMALL=2
    START=3
    END=4
class Cave:
    def __init__(self,name):
        if name=="start":
            self.size= Size.START
        elif name=="end":
            self.size= Size.END
        elif name.isupper():
            self.size = Size.BIG
        else:
            self.size = Size.SMALL
        self.neighbors = []
        self.name = name

    def add_neighbor(self,neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
    def __repr__(self):
        return self.name
def contains(list,filter):
    for x in list:
        if filter(x):
            return True
    return False

def valid_path(n, path_head):
    small_caves = [x for x in path_head if x.size == Size.SMALL]
    if n.size == Size.START:
        return False
    elif n.size == Size.SMALL:
        count_small = Counter(small_caves).values()
        # if we have 2 small caves already, and this one already
        # exists, cannot visit twice
        if 2 in count_small and n in path_head:
            return False
    return True


with open("input.txt") as f:
    lines = f.readlines()
    caves =[]
    for line in lines:
        line = line.strip()
        one,two = line.split('-')
        cave_one, cave_two = None,None
        if not contains(caves, lambda x: x.name == one):
            cave_one = Cave(one)
            caves.append(cave_one)
        else:
            cave_one = [x for x in caves if x.name==one][0]
        if not contains(caves,lambda x: x.name==two):
            cave_two = Cave(two)
            caves.append(cave_two)
        else:
            cave_two = [x for x in caves if x.name==two][0]
        cave_one.add_neighbor(cave_two)
        cave_two.add_neighbor(cave_one)
    paths = [[x for x in caves if x.size == Size.START]]
    finished_paths = []
    while(len(paths) > 0):
        #get pointer to first path
        path_head = paths[0]
        paths.pop(0)
        for n in path_head[-1].neighbors:
            if n.size == Size.END:
                finished_paths.append(path_head+[n])
            elif valid_path(n, path_head):
                paths.append(path_head + [n])
    print(len(finished_paths))
