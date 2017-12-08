class OxoBoard:
    loc = [] # locations on
    def __init__(self):
        """Fills Board loc with 0"""
        for i in range(0,3):
            temp = []
            for j in range(0,3):
                temp.append(0)
            self.loc.append(temp)

    def get_square(self, x, y):
        """Returns Value Of Square"""
        return self.loc[x][y]

    def set_square(self, x, y, mark):
        """Sets Value Of A Square"""
        if self.loc[x][y] == 0:
            self.loc[x][y]=mark
            return True
        else:
            return False

    def is_board_full(self):
        """Checks If The Board Is Full, Returns True If Board Is Full"""
        for x in range(0,3):
            for y in range(0,3):
                if self.loc[x][y] == 0:
                    return False
        return True


    def get_winner(self):
        """ Checks If there is a winner in the game returns 0 if no winner or 1/2 depending on winner"""
        for x in range(0,3):  # checks vertical
            for win in range(1,3):
                if self.loc[x][0] == win and self.loc[x][1] == win and self.loc[x][2] == win:
                    return win
        for y in range(0,3):  # checks horizontal
            for win in range(1,3):
                if self.loc[0][y] == win and self.loc[1][y] == win and self.loc[2][y] == win:
                    return win
        for win in range(1, 3):  # checks diagonal
            for i in range(0, 2):
                if self.loc[2*i][0] == win and self.loc[1][1] == win and self.loc[2-(2*i)][2] == win:
                    return win
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
