class OxoBoard:
    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.col = len(self.board)
        self.row = len(self.board[0])


    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
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
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """

        for y in xrange(0, self.row):
            for x in xrange(0, self.col):
                if self.board[x][y] == 0:
                    return False
        return True





    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """

        for x in xrange(0, self.row):
            if (self.board[x][0] == 1 and self.board[x][1] == 1 and self.board[x][2] == 1) or (self.board[0][x] == 1 and self.board[1][x] == 1 and self.board[2][x] == 1):
                return 1

        if (self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1) or (self.board[2][0] == 1 and self.board[1][1] == 1 and self.board[0][2] == 1):
            return 1

        for x in range(0, self.row):
            if (self.board[x][0] == 2 and self.board[x][1] == 2 and self.board[x][2] == 2) or (self.board[0][x] == 2 and self.board[1][x] == 2 and self.board[2][x] == 2):
                return 2

        if (self.board[0][0] == 2 and self.board[1][1] == 2 and self.board[2][2] == 2) or (self.board[2][0] == 2 and self.board[1][1] == 2 and self.board[0][2] == 2):
            return 2

        return 0


    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in xrange(3):
            if y > 0:
                print "--+---+--"
            for x in xrange(3):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print
