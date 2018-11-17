class OxoBoard:
    """ NB: implementation in this class is intentionally obfuscated
        so that you can't copy it for your worksheet submission :) """

    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        self.board = [0]*9

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.board[y*3 + x]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        i = y*3 + x
        if self.board[i] == 0:
            self.board[i] = mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        return 0 not in self.board

    def check_line(self, start, delta):
        p = self.board[start]
        return p if p == self.board[start+delta] == self.board[start+2*delta] else 0

    def check_lines(self):
        for i in range(3):
            yield self.check_line(i*3, 1)   # horizontal
            yield self.check_line(i, 3)     # vertical

        # Diagonals
        yield self.check_line(0, 3+1)
        yield self.check_line(2, 3-1)

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        try:
            return [c for c in self.check_lines() if c != 0][0]
        except IndexError:
            return 0

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
