class OxoBoard:
    empty = 0

    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        self.tile_width = 3
        self.tile_height = 3
        self.tile = [[0 for y in range(self.tile_width)]
                     for x in xrange(self.tile_height)]

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.tile[x][y]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.tile[x][y] == self.empty:
            self.tile[x][y] = mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        for x in xrange(self.tile_width):
            for y in xrange(self.tile_height):
                if self.tile[x][y] == self.empty:
                    return False

        return True

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        for i in xrange(3):
            for j in xrange(3):
                compare = self.tile[i][j]

                if compare == self.empty:
                    continue

                for vector in [(1, 0), (1, 1), (0, 1), (-1, 1)]:
                    try:
                        box_to_check = [i, j]
                        char_to_check_for = self.tile[i][j]
                        for x in range(1, 3):
                            box_to_check[0] += vector[0]
                            box_to_check[1] += vector[1]

                            if self.tile[box_to_check[0]][box_to_check[1]] != char_to_check_for:
                                break

                            if box_to_check[0] >= self.tile_width or\
                                    box_to_check[1] >= self.tile_height or\
                                    box_to_check[0] < 0 or\
                                    box_to_check[1] < 0:
                                break

                            if x == 2:
                                return compare

                    except:
                        continue

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
