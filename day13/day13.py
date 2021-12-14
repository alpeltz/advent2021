import numpy as np
class Grid:
    def __init__(self):
        self.data = np.zeros((1,1))
    def add_row(self):
        self.data = np.r_[self.data, np.zeros((1,self.data.shape[1]))]
    def add_col(self):
        self.data = np.c_[self.data, np.zeros((self.data.shape[0],1))]
    def mark(self, x,y):
        while x >= self.data.shape[1]:
            self.add_col()
        while y >= self.data.shape[0]:
            self.add_row()
        self.data[y][x] = 1
    def flip(self,axis,val):
        for (i,row) in enumerate(self.data):
            for (j,col) in enumerate(row):
                if axis=="x" and j > val:
                    new_x = -j + 2*val
                    self.data[i][new_x] = self.data[i][new_x] or col
                    self.data = self.data[:,:val]
                if axis=="y" and i > val:
                    new_y = -i + 2*val
                    self.data[new_y][j] = self.data[new_y][j] or col
                    self.data = self.data[:val,:]
 
with open("input.txt") as f:
    grid = Grid()
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if ',' in line:
            x,y = line.split(',')
            grid.mark(int(x),int(y))
        elif not len(line)==0:
            axis, val = line.split(' ')[2].split('=')
            val = int(val)
            grid.flip(axis,val)
            print(np.sum(grid.data))
    for row in grid.data:
        for col in row:
            if col:
                print("#",end="")
            else:
                print(".",end="")
        print()
