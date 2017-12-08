class OxoTile:
    EMPTY = 0
    O = 1
    X = 2


class OxoBoard:
    grid = None  # multidimensional [x][y] list of OxoTile values
    num_rows = 3  # number of rows on the board
    num_cols = 3  # number of columns on the board
    winning_row_length = 3  # number of Xs or Os in a row to win

    def __init__(self, num_rows=3, num_cols=3, winning_row_length=3):
        """ The initialiser.
        Args:
            num_rows: number of rows on the grid (y size)
            num_cols: number of columns of the grid (x size)
            winning_row_length: the number of Xs or Os in a row to win
        """
        # Initialise variables
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.winning_row_length = winning_row_length

        # Create the 2-dimensional array for the grid of squares
        self.grid = [[0 for y in xrange(self.num_rows)] for x in xrange(self.num_cols)]

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.grid[x][y]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False.
        """
        if self.grid[x][y] is OxoTile.EMPTY:
            self.grid[x][y] = mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True.
        """
        # Return whether an empty square was (not!) found in any of the grid's column arrays
        return not any(OxoTile.EMPTY in column for column in self.grid)

    def get_winner(self):
        """ If a player has [winning_row_length] in a row, return 1 or 2 depending on which player.
            Otherwise, return 0.
        """
        # Declare a search direction list, representing the XY offsets of
        # up-right, right, down-right and down directions. These are the
        # directions we'll search the grid along for matching O's or X's
        dir_xy_offsets = [(1, 0), (1, 1), (1, -1), (0, 1)]

        # Iterate through all squares in the grid and search each possible line direction
        for start_x in xrange(0, self.num_cols):
            for start_y in xrange(0, self.num_rows):
                compare_type = self.grid[start_x][start_y]

                # Don't search along empty tiles
                if compare_type == OxoTile.EMPTY:
                    continue

                # Search along the four directions to see if there's a valid row
                for offset in dir_xy_offsets:
                    for step in xrange(1, self.winning_row_length):
                        # Step
                        current_x = start_x + offset[0] * step
                        current_y = start_y + offset[1] * step

                        # Don't go past the border!
                        if current_x >= self.num_cols or current_y >= self.num_rows or \
                                current_y < 0:
                            break

                        # If this square dares to be different, this isn't a winner
                        if self.grid[current_x][current_y] is not compare_type:
                            break

                        # If we found winning_row_length matching squares along this line, we won!
                        if step == self.winning_row_length - 1:
                            return compare_type  # This is the winner!

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
