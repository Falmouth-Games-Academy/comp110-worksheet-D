class OxoBoard:

    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        self.number_to_win_for = 3
        self.rows = 3
        self.cols = 3

        self.numberOfTiles = self.rows * self.cols

        self.board = []
        for row in range(self.rows):
            self.board += [[0] * self.cols]
        print self.board
        #raise NotImplementedError("TODO: implement __init__")

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.board[y][x]
        #raise NotImplementedError("TODO: implement get_square")

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.get_square(x, y) == 0:
            self.board[y][x] = mark
            return True
        else:
            return False
        #raise NotImplementedError("TODO: implement set_square")

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """

        tilesChecked = 0

        for row in self.board:
            for item in row:
                if item != 0:
                    tilesChecked += 1
                    if tilesChecked == self.numberOfTiles:
                        return True
        #raise NotImplementedError("TODO: implement is_board_full")


    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """

        p1_Count = 0
        p2_Count = 0
        hRow = 0
        vRow = 0

        # check rows
        for row in self.board:
            for item in row:
                if item == 1:
                    p1_Count += 1
                elif item == 2:
                    p2_Count += 1
            if p1_Count == self.number_to_win_for:
                return 1
            elif p2_Count == self.number_to_win_for:
                return 2
            else:
                p1_Count = 0
                p2_Count = 0

        # do 3 checks
        for i in range(3):

            # check columns
            for row in self.board:
                if row[hRow] == 1:
                    p1_Count += 1
                elif row[hRow] == 2:
                    p2_Count += 1

            if p1_Count == self.number_to_win_for:
                return 1
            elif p2_Count == self.number_to_win_for:
                return 2
            else:
                p1_Count = 0
                p2_Count = 0
                hRow += 1

        return 0



        #raise NotImplementedError("TODO: implement get_winner")

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
