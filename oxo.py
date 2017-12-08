class OxoBoard:
    # Set the variables for the size of the board.
    board_width = 3
    board_height = 3

    def __init__(self):
        # Create a matrix to identify the board positions, all set to 0 at the start.
        self.matrix = [[0] * self.board_width for rows in xrange(self.board_height)]

    def get_square(self, x, y):
        # Returns the position on the board using indexing,
        # x being the column, y being the row.
        return self.matrix[x][y]

    def set_square(self, x, y, mark):
        # If the value is 0 in the board (ie empty) then that position
        # is available to be marked as X or O.
        if self.matrix[x][y] == 0:
            self.matrix[x][y] = mark
            return True
        else:
            return False

    def is_board_full(self):
        # Checks if any of the positions on the board are empty
        # (value is 0 if empty).
        for x in xrange(0, self.board_width):
            for y in xrange(0, self.board_height):
                if self.matrix[x][y] == 0:
                    return False
        return True

    def get_winner(self):
        """ Visual representation to help with the indexing to compare
        board positions.           y  y  y
        0 [0, 1, 2]             x [0, 0, 0]
        1 [0, 1, 2]      =      x [0, 0, 0]
        1 [0, 1, 2]             x [0, 0, 0]
        """

        # This checks for both players board mark positions.
        for winner in xrange(1, 3):
            # This checks each row.
            for x in xrange(0, self.board_width):
                # This checks if the horizontal positions on the board have the
                # players mark in every position in that row.
                if (self.matrix[x][0] == winner) and (self.matrix[x][1] == winner)\
                        and (self.matrix[x][2] == winner):
                    return winner
            # This does the same as above but with each column instead of row.
            for y in xrange(0,self.board_height):
                if (self.matrix[0][y] == winner) and (self.matrix[1][y] == winner) \
                        and (self.matrix[2][y] == winner):
                    return winner
            # These IF statements check the diagonal positions for the players
            # marks to check for a win.
            if (self.matrix[0][0] == winner) and (self.matrix[1][1] == winner) \
                    and (self.matrix[2][2] == winner):
                return winner
            if (self.matrix[2][0] == winner) and (self.matrix[1][1] == winner) \
                    and (self.matrix[0][2] == winner):
                return winner
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
