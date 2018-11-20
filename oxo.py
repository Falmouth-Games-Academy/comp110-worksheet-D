class OxoBoard:
    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        # nested list of square contents
        self.square = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square."""
        return self.square[y][x]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.square[y][x] == 0:
            self.square[y][x] = mark
            return True
        else:
            return False
        # raise NotImplementedError("TODO: implement set_square")

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        pass
        # raise NotImplementedError("TODO: implement is_board_full")

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        return 0
        # raise NotImplementedError("TODO: implement get_winner")

    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in range(3):
            if y > 0:
                print("--+---+--")
            for x in range(3):
                if x > 0:
                    print('|',)

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print(" OX"[self.get_square(x, y)],)
            print
