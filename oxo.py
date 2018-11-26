class OxoBoard:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        '''
        y   =     0,1,2
        board = [[a,b,c], x = 0 
                 [d,e,f], x = 1
                 [g,h,i]] x = 2
        '''

    def get_square(self, x, y):
        return self.board[x][y]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.board[x][y] == 0:
            self.board[x][y] = mark
            return True
        else:
            return False

    def is_board_full(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 0:
                    return False
        return True

    def get_winner(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2]:
            return int(self.board[0][0])
        elif self.board[1][0] == self.board[1][1] == self.board[1][2]:
            return int(self.board[1][0])
        elif self.board[2][0] == self.board[2][1] == self.board[2][2]:
            return int(self.board[2][0])
        elif self.board[0][0] == self.board[1][0] == self.board[2][0]:
            return int(self.board[0][0])
        elif self.board[0][1] == self.board[1][1] == self.board[2][1]:
            return int(self.board[0][1])
        elif self.board[0][2] == self.board[1][2] == self.board[2][2]:
            return int(self.board[0][2])
        elif self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return int(self.board[0][0])
        elif self.board[2][0] == self.board[1][1] == self.board[0][2]:
            return int(self.board[2][0])
        else:
            return 0

    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in range(3):
            if y > 0:
                print("--+---+--")
            for x in range(3):
                if x > 0:
                    print('|',)

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print(" OX"[self.get_square(x, y)],)
            print
