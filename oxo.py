class OxoBoard:
    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        self.number_to_win_for = 3
        self.rows = 3
        self.cols = 3

        self.numberOfTiles = self.rows * self.cols

        # Create and initialise the game board
        self.board = []
        for row in range(self.rows):
            self.board += [[0] * self.cols]
        print self.board

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.board[y][x]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        
        if self.get_square(x, y) == 0:
            self.board[y][x] = mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """

        # number of tiles on the board
        tiles_checked = 0

        # goes through each tile and checks if they are filled or not
        for row in self.board:
            for item in row:
                if item != 0:
                    tiles_checked += 1
                    if tiles_checked == self.numberOfTiles:
                        return True

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """

        # Player score for each row check
        p1_count = 0
        p2_count = 0

        # item/row counters
        v_row = 0
        d_item = 0
        d_item2 = 2

        # check diagonal row
        for row in self.board:
            if row[d_item] == 1:
                p1_count += 1
            elif row[d_item] == 2:
                p2_count += 1
            else:
                p1_count = 0
                p2_count = 0
            d_item += 1
        if p1_count == self.number_to_win_for:
            return 1
        elif p2_count == self.number_to_win_for:
            return 2
        else:
            p1_count = 0
            p2_count = 0

        # check diagonal row
        for row in self.board:
            if row[d_item2] == 1:
                p1_count += 1
            elif row[d_item2] == 2:
                p2_count += 1
            else:
                p1_count = 0
                p2_count = 0
            d_item2 -= 1
        if p1_count == self.number_to_win_for:
            return 1
        elif p2_count == self.number_to_win_for:
            return 2
        else:
            p1_count = 0
            p2_count = 0

        # check horizontal rows
        for row in self.board:
            for item in row:
                if item == 1:
                    p1_count += 1
                elif item == 2:
                    p2_count += 1
            if p1_count == self.number_to_win_for:
                return 1
            elif p2_count == self.number_to_win_for:
                return 2
            else:
                p1_count = 0
                p2_count = 0

        # do 3 checks
        for i in range(3):
            # check vertical rows
            for row in self.board:
                if row[v_row] == 1:
                    p1_count += 1
                elif row[v_row] == 2:
                    p2_count += 1

            if p1_count == self.number_to_win_for:
                return 1
            elif p2_count == self.number_to_win_for:
                return 2
            else:
                p1_count = 0
                p2_count = 0
                v_row += 1

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
