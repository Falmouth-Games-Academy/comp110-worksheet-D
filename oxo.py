class OxoBoard:

    board = {}

    winningCombinations = \
    [
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]
    ]

    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        for x in xrange(3):
            for y in xrange(3):
                self.board[x,y] = 0
        #raise NotImplementedError("TODO: implement __init__")

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.board[x,y]
        #raise NotImplementedError("TODO: implement get_square")

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.board[x,y] == 0:
            self.board[x,y] = mark
            return True
        else:
            return False
        #raise NotImplementedError("TODO: implement set_square")

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        for x in xrange(3):
            for y in xrange(3):
                if self.board[x,y] == 0:
                    return False
        return True
        #raise NotImplementedError("TODO: implement is_board_full")

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        for i in self.winningCombinations:
            oMark = 0
            xMark = 0
            for j in xrange(3):
                x,y = i[j][0],i[j][1]
                if self.board[x,y] == 1:
                    oMark += 1
                elif self.board[x,y] == 2:
                    xMark += 1
                else:
                    print "Exceptional Error neither O nor X"

            if oMark >= 3:
                return 1
            elif xMark >= 3:
                return 2

        return 0
        #raise NotImplementedError("TODO: implement get_winner")

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
