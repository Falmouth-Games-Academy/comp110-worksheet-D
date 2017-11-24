class OxoTile:
    EMPTY = 0
    X = 1
    O = 2


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
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.winning_row_length = winning_row_length
        self.grid = [[0 for y in xrange(self.num_rows)] for x in xrange(self.num_cols)]

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.grid[x][y]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.grid[x][y] is not OxoTile.EMPTY:
            return False

        self.grid[x][y] = mark
        return True

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        # Loop through all tiles and return False if an empty one is found
        for x in xrange(0, self.num_cols):
            for y in xrange(0, self.num_rows):
                if self.grid[x][y] == OxoTile.EMPTY:
                    return False

        return True

    def get_winner(self):
        """ If a player has [winning_row_length] in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        # Declare a search direction list, representing up-right, right,
        # down-right and down directions in xy tuples
        dir_xy = [(1, 0), (1, 1), (1, -1), (0, 1)]

        # Iterate through all items in list
        for x in xrange(0, self.num_cols):
            for y in xrange(0, self.num_rows):
                compare_type = self.grid[x][y]

                if compare_type == OxoTile.EMPTY:
                    continue

                # Search all directions to see if there's a valid row
                for dir_id in xrange(0, 4):
                    for p in xrange(1, self.winning_row_length):
                        pos_x = x + dir_xy[dir_id][0] * p
                        pos_y = y + dir_xy[dir_id][1] * p

                        if pos_x >= self.num_cols or pos_y >= self.num_rows or \
                            pos_x < 0 or pos_y < 0:
                            break

                        if self.grid[pos_x][pos_y] is not compare_type:
                            break
                        if p == self.winning_row_length - 1:
                            return compare_type  # Winner!

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
