class OxoBoard:
    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        self.size = 3
        self.board = [[0 for x in range(self.size)] for y in range(self.size)]
        '''
         x = 1,2,3
           [[a,b,c], y = 0
            [d,e,f], y = 1
            [g,h,i]] y = 2      i think
            
            it'd be pretty easy to implement bigger boards for this, need:
            -> a screen that asks players how big they want the board
            -> this __init__ to have an extra parameter for board size
                -> this parameter also determines grid_width/height in play.py,
                 the screen size would stay the same, but the boxes are smaller
            -> the new parameter would be assigned to self.size
            -> searches for non-diagonal wins would have to be updated, as they
                are currently hard coded because it was nice and easy :(
                
            pep-8 is lame so I didn't stick too strictly to it,
            comments are sparse because doc-strings exist :)
        '''

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.board[y][x]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.board[y][x] == 0:
            self.board[y][x] = mark
            return True
        else: return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        for x in range(self.size):
            for y in range(self.size):
                if self.board[y][x] == 0: return False
        return True

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """

        # Horizontal
        for y in range(3):
            if self.board[y][0] != 0 and \
                    self.board[y][0] == self.board[y][1] == self.board[y][2]:
                return self.board[y][0]

        # Vertical
        for x in range(3):
            if self.board[0][x] != 0 and \
                    self.board[0][x] == self.board[1][x] == self.board[2][x]:
                return self.board[0][x]

        # Diagonals
        for diagonal in range(0,self.size,self.size-1):
            # first iteration looks and -ve diagonal, second at +ve diagonal
            mark = None
            possible = True
            while possible:
                for y in range(self.size):
                    x = abs(diagonal - y)
                    if mark is None:
                        mark = self.board[y][x]
                    else:
                        if mark != self.board[y][x]:
                            possible = False
                if possible: return mark
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