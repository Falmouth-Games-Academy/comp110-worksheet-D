class OxoBoard:
    # Set the variables for the size of the board.
    board_width = 3
    board_height = 3

    def __init__(self):
        # Create a matrix to identify the board positions, all set to 0 at the start.
        self.matrix = [[0,0,0],[0,0,0],[0,0,0]]

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
        board positions.
        0 [0, 1, 2]
        1 [0, 1, 2]
        1 [0, 1, 2]
        """

        # Checks if there is a winning combination for player 1 by comparing
        # the values on the board to each winning combination.
        if (self.matrix[0][0] == self.matrix[1][0] == self.matrix[2][0] == 1) or \
                (self.matrix[0][1] == self.matrix[1][1] == self.matrix[2][1] == 1) or \
                (self.matrix[0][2] == self.matrix[1][2] == self.matrix[2][2] == 1) or \
                (self.matrix[0][0] == self.matrix[0][1] == self.matrix[0][2] == 1) or \
                (self.matrix[1][0] == self.matrix[1][1] == self.matrix[1][2] == 1) or \
                (self.matrix[2][0] == self.matrix[2][1] == self.matrix[2][2] == 1) or \
                (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == 1) or \
                (self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == 1):
            return 1

        # Checks if there is a winning combination for player 2 by comparing
        # the values on the board to each winning combination.
        if (self.matrix[0][0] == self.matrix[1][0] == self.matrix[2][0] == 2) or \
                (self.matrix[0][1] == self.matrix[1][1] == self.matrix[2][1] == 2) or \
                (self.matrix[0][2] == self.matrix[1][2] == self.matrix[2][2] == 2) or \
                (self.matrix[0][0] == self.matrix[0][1] == self.matrix[0][2] == 2) or \
                (self.matrix[1][0] == self.matrix[1][1] == self.matrix[1][2] == 2) or \
                (self.matrix[2][0] == self.matrix[2][1] == self.matrix[2][2] == 2) or \
                (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == 2) or \
                (self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == 2):
            return 2

        else:
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
