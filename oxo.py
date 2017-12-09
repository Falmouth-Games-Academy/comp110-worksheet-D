class OxoBoard:
    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        #sets the number of rows and collems there are
        self.rows = 3
        self.columns = 3

        self.numberOfTiles = self.rows * self.columns

        self.board = []
        for row in range(self.rows):
            self.board += [[0] * self.columns]
        print self.board
        #raise NotImplementedError("TODO: implement __init__")

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        #retuns the state of the square the mouse is over
        return self.board[y][x]
        #raise NotImplementedError("TODO: implement get_square")

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        #if the number which is retuned above is 0 then it but the player mark on the square
        if self.get_square(x, y) == 0:
            self.board[y][x] = mark
            return True
        else:
            return False
        #raise NotImplementedError("TODO: implement set_square")

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        # see if the board is filled
        tiles_filled = 0

        for row in self.board:
            for item in row:
                if item != 0:
                    tiles_filled += 1
                    if tiles_filled == self.numberOfTiles:
                        return True
        #raise NotImplementedError("TODO: implement is_board_full")

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        number_to_win_for = 3

        p1_Count = 0
        p2_Count = 0

        hRow = 0

        for row in self.board:
            if row[hRow] == 1:
                p1_Count += 1
            elif row[hRow] == 2:
                p2_Count += 1
            else:
                return 0
        hRow += 1

        if p1_Count == number_to_win_for:
            return 1
        if p2_Count == number_to_win_for:
            return 2

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