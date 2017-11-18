class OxoBoard:

    # Empty = 0, O = 1, X = 2

    board = {}

    strike_combinations = [
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (0, 2)],
    ]

    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        for x in xrange(3):
            for y in xrange(3):
                self.board[x, y] = 0

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.board[x, y]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.board[x, y] == 0:
            self.board[x, y] = mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        for x in xrange(3):
            for y in xrange(3):
                if self.board[x, y] == 0:
                    return False
        return True

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        for line in self.strike_combinations: # For each strike combination
            o_strike = 0
            x_strike = 0
            for element in xrange(3): # For each position for strike line
                x, y = line[element][0], line[element][1]
                if self.board[x, y] == 1: # If O is there
                    o_strike += 1 # Three is a strike
                elif self.board[x, y] == 2: # If X is there
                    x_strike += 1 # Three is a strike

            if o_strike >= 3:
                return 1
            elif x_strike >= 3:
                return 2

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
