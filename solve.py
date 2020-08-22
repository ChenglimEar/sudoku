class Solver:
    def __init__(self,board,choices=None):
        if choices is None:
            choices = {}
        self.board = board
        
    def valid_in_box(self,x,y,num):
        box_x = (x // 3) * 3
        box_y = (y // 3) * 3
        for rel_x in range(3):
            for rel_y in range(3):
                if self.board[box_y+rel_y][box_x+rel_x] == num:
                    return False
        return True
            
    def valid_in_horz(self,y,num):
        for x in range(9):
            if self.board[y][x] == num:
                return False
        return True
    
    def valid_in_vert(self,x,num):
        for y in range(9):
            if self.board[y][x] == num:
                return False
        return True
    
    def find_empty(self):
        for x in range(len(self.board[0])):
            for y in range(len(self.board)):
                if self.board[y][x] == 0:
                    return (x,y)
        return None
    
    def solve(self):
        """The primary method to call to solve the board in this class"""

        pos = self.find_empty()
        if pos is None:
            return True
        x,y = pos
        for i in range(1,10):
            # check num in box
            if self.valid_in_box(x,y,i) and self.valid_in_horz(y,i) and self.valid_in_vert(x,i):
                self.board[y][x] = i
                # keep checking the next open slot
                if self.solve():
                    return True
                else:
                    # didn't pan out, so undo and continue to try another number
                    self.board[y][x] = 0
        return False
                                        
    def print_board(self):
        """Call this to print the current state of the board"""

        for i in range(9):
            print(self.board[i])
                
if __name__ == '__main__':
    board = [[3,0,6,5,0,8,4,0,0],
             [5,2,0,0,0,0,0,0,0],
             [0,8,7,0,0,0,0,3,1],
             [0,0,3,0,1,0,0,8,0],
             [9,0,0,8,6,3,0,0,5],
             [0,5,0,0,9,0,6,0,0],
             [1,3,0,0,0,0,2,5,0],
             [0,0,0,0,0,0,0,7,4],
             [0,0,5,2,0,6,3,0,0]]
    solver = Solver(board)
    solver.print_board()
    print()
    if solver.solve():
        solver.print_board()
    else:
        print("No Solution!")

