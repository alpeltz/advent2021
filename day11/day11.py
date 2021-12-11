class Octopus:
    def __init__(self, val):
        self.neighbors = []
        self.energy = val
        self.flashed = False 
    def add_neighbor(self,i,j,grid):
        if i > len(grid)-1 or i < 0:
            return
        if j > len(grid[i])-1 or j < 0:
            return
        self.neighbors.append(grid[i][j])

    def add_neighbors(self, i,j, grid):
        #top left
        self.add_neighbor(i-1,j-1,grid)
        #top center
        self.add_neighbor(i-1,j,grid)
        #top right
        self.add_neighbor(i-1,j+1,grid)
        #mid left
        self.add_neighbor(i,j-1,grid)
        #mid right
        self.add_neighbor(i,j+1,grid)
        #bottom left
        self.add_neighbor(i+1,j-1,grid)
        #bottom center
        self.add_neighbor(i+1,j,grid)
        #bottom right
        self.add_neighbor(i+1,j+1,grid)

    def flash(self, total_flashes):
        self.flashed=True
        for n in self.neighbors:
            n.increase(total_flashes)
            
    def reset_flash(self):
        if self.flashed:
            self.energy=0
            self.flashed=False
            return True
        return False
    def increase(self,total_flashes):
        self.energy +=1
        if self.energy > 9 and not self.flashed:
            total_flashes["key"]+=1
            self.flash(total_flashes)
    def __repr__(self):
        return str(self.energy)


with open("input.txt") as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        row = []
        line = line.strip()
        for o in line:
            row.append(Octopus(int(o)))
        grid.append(row)
    for (i,row) in enumerate(grid):
        for (j,col) in enumerate(row):
            col.add_neighbors(i,j,grid)
    total_flashes={"key":0}
    for i in range(300):
        for row in grid:
            for col in row:
                col.increase(total_flashes)
        # after all vals were increased
        sync =0
        for row in grid:
            for col in row:
                if(col.reset_flash()):
                    sync+=1
        if(sync==100):
            print("Syncronized at step ", i+1)
            break;
    print(total_flashes)

