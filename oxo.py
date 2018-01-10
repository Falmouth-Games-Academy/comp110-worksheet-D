#I don't know whats gone wrong...
class OxoBoard:
    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        OxoBoard.board = [[0]*3]*3


    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return OxoBoard.board[y][x]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if OxoBoard.board[y][x] == 0:
            OxoBoard.board[y][x] = mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        for y in OxoBoard.board:
            for x in y:
                if x == 0:
                    return False
        return True

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        for y in OxoBoard.board:
            if y[0] == y[1] == y[2]:
                if y[0] != 0:
                    return y[0]
        for x in xrange(3):
            if OxoBoard.board[0][x] == OxoBoard.board[1][x] == OxoBoard.board[2][x]:
                if OxoBoard.board[0][x] != 0:
                    return OxoBoard.board[0][x]
        if OxoBoard.board[0][0] == OxoBoard.board[1][1] == OxoBoard.board[2][2] or\
            OxoBoard.board[0][2] == OxoBoard.board[1][1] == OxoBoard.board[2][0]:
            if OxoBoard.board[1][1] != 0:
                return OxoBoard.board[1][1]
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

game = OxoBoard()