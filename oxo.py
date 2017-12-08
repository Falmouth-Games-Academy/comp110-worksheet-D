class OxoBoard:
    empty = 0

    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        self.tile_width = 3  # Width of the game board in tile (squares)
        self.tile_height = 3  # Height of the game board in tile (squares)
        self.winning_condition = 3  # Same marks in a row in order to win
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
        for x in xrange(self.tile_width):
            for y in xrange(self.tile_height):

                # Checks if there are still empty tiles
                # If there are - continue the loop
                if self.tile[x][y] == self.empty:
                    continue

                # Loops through 4 different direction to determine
                # whether a player has reached 3 in a row (winning condition)
                for vector in [(1, 0), (1, 1), (0, 1), (-1, 1)]:
                    try:
                        tile_to_check = [x, y]
                        mark_to_check_for = self.tile[x][y]

                        for i in range(1, self.winning_condition):
                            tile_to_check[0] += vector[0]
                            tile_to_check[1] += vector[1]

                            # Checks tiles to prevent unfair winning
                            if self.tile[tile_to_check[0]][tile_to_check[1]]\
                                    != mark_to_check_for:
                                break

                            # Checks tiles to prevent unfair winning
                            if tile_to_check[0] >= self.tile_width or\
                                    tile_to_check[1] >= self.tile_height or\
                                    tile_to_check[0] < 0 or\
                                    tile_to_check[1] < 0:
                                break

                            # Returns number of a winner (1 or 2)
                            if i == (self.winning_condition - 1):
                                return self.tile[x][y]

                    except:
                        continue

        # If nothing of above happened - returns 0 (draw)
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
