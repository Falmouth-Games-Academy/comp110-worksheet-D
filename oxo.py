class OxoBoard:
    #BoardWidth = 3
    #BoardHeight = 3
    #BoardSquares = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    def __init__(self):
        self.GameBoard = [[0 for x in range(3)] for y in range(3)]


    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.GameBoard[x][y]


    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.get_square(x, y) == 0:
            self.GameBoard[x][y] = mark
            return True
        return False


    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        for x in xrange(3):
            for y in xrange(3):
                if self.GameBoard[x][y] == 0:
                    return False
        return True


    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        for player in [1,2]:  # check row
            for x in range(0,3):
                if self.GameBoard[x][0] == player and self.GameBoard[x][1] == player and self.GameBoard[x][2] == player:
                    return player
            for y in range(0,3):  # check column
                if self.GameBoard[0][y] == player and self.GameBoard[1][y] == player and self.GameBoard[2][y] == player:
                    return player
            if self.GameBoard[0][0] == player and self.GameBoard[1][1] == player and self.GameBoard[2][2] == player:
                return player
            if self.GameBoard[2][0] == player and self.GameBoard[1][1] == player and self.GameBoard[0][2] == player:
                return player
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
