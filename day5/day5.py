import numpy as np


class VentMap:
    def __init__(self):
        self.data = np.zeros((1,1))
    def add_row(self):
        self.data = np.r_[self.data, np.zeros((1,self.data.shape[1]))]
    def add_col(self):
        self.data = np.c_[self.data, np.zeros((self.data.shape[0], 1))]
    def mark(self, coord):
        x,y = coord
        while x >= self.data.shape[1]:
            self.add_col()
        while y >= self.data.shape[0]:
            self.add_row()
        self.data[y][x] += 1
    def mark_row(self, p1,p2):
        x1,y1 = p1
        x2,y2 = p2
        # diagonal lines will have a slope of 1/-1
        if (x2 != x1) and ((y2-y1)/(x2-x1))**2 ==1:
            if x1 > x2:
                xstep =-1
                x2 -=1
            else:
                xstep=1
                x2+=1
            if y1>y2:
                ystep=-1
                y2-=1
            else:
                ystep=1
                y2+=1
            xcoords = np.arange(x1,x2,xstep)
            ycoords=np.arange(y1,y2,ystep)
            for (enum,i) in enumerate(xcoords):
                j = ycoords[enum]
                self.mark((i,j))

        if x1 == x2:
            if y1 > y2:
                temp = y1
                y1 = y2
                y2 = temp
            for i in range(y1,y2+1):
                self.mark((x1,i))
        if y1 == y2:
            if x1 > x2:
                temp = x1
                x1 = x2
                x2 = temp
            for i in range(x1,x2+1):
                self.mark((i,y1))
with open("input.txt") as f:
    lines = f.readlines()
    m = VentMap()
    for line in lines:
        coords = line.strip().split(' -> ')
        x1,y1 = coords[0].split(',')
        x2,y2 = coords[1].split(',')
        m.mark_row((int(x1),int(y1)),(int(x2),int(y2)))
    print(m.data[m.data > 1].size)
