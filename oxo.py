
class OxoBoard:
    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """

        """These variables will set the height/width of the board and the condition to win"""
        self.oxoboard = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
            """ This takes the x and y co-ordinates and returns them based on the board positions """
            return self.oxoboard[x][y]

        raise NotImplementedError("TODO: implement get_square")

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        raise NotImplementedError("TODO: implement set_square")

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. ""
          
        for y in xrange(0, self.row):
              for x in xrange(0, self.col):
                  if self.board[x][y] == 0:
                  
        raise NotImplementedError("TODO: implement is_board_full")

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        raise NotImplementedError("TODO: implement get_winner")

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
