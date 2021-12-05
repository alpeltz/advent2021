class BingoBoard:
    
    def __init__(self):
        self.data = {}
    def __init__(self, board):
        self.data = {}
        self.marked_rows = {}
        self.marked_cols = {}
        self.tlbr = 0
        self.trbl = 0
        lines = board.strip().split('\n')
        for (i,y) in enumerate(lines):
            y = y.strip()
            for(j,x) in enumerate(y.split()):
                # create a dict that maps each value to the ij coordinate and
                # the bool to decide if it is marked
                if i not in self.marked_rows:
                    self.marked_rows[i] = 0
                if j not in self.marked_cols:
                    self.marked_cols[j] = 0
                self.data[x] = [i,j,False]
    def mark_val(self, val):
        if val in self.data:
           v = self.data[val]
           v[2] = True
           self.marked_rows[v[0]] = self.marked_rows[v[0]] + 1
           self.marked_cols[v[1]] = self.marked_cols[v[1]] + 1
           if v[0] == v[1]:
               self.tlbr = self.tlbr + 1
           if v[1] == -v[0] + 4:
               self.trbl = self.trbl + 1

    def has_bingo(self):
        if any([x >= 5 for x in self.marked_rows.values()]):
            return True
        if any([x >= 5 for x in self.marked_cols.values()]):
            return True
        return False
        # return self.tlbr >= 5 or self.trbl >= 5
    def print_winner(self, last_call):
        total = 0
        for x in self.data:
            if not self.data[x][2]:
                total += int(x)
        print(total*int(last_call))
with open("input.txt") as f:
    lines = f.readlines()
    calls = lines[0].split(",")
    call_idx=-1
    def last_bingo(boards):
        if len(boards) <= 1 and boards[0].has_bingo():
            print("Winner: ", boards[0].data)
            boards[0].print_winner(calls[call_idx])
            return True

    boards = "".join(lines[1:]).split("\n\n")
    board1 = BingoBoard(boards[0])
    boards = [BingoBoard(board) for board in boards]
    while(not last_bingo(boards)):
        call_idx+=1
        boards_to_remove = []
        for b in boards:
            b.mark_val(calls[call_idx])
            if len(boards) > 1 and b.has_bingo():
                boards_to_remove.append(b)
        for r in boards_to_remove:
            boards.remove(r)

    f.close()


