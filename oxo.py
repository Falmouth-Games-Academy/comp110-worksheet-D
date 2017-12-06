class OxoBoard:

    board_width = 3
    board_height = 3


    def __init__(self):
        self.matrix = [[0,0,0],[0,0,0],[0,0,0]]

    def get_square(self, x, y):

        return self.matrix[x][y]

    def set_square(self, x, y, mark):

        if self.matrix[x][y] == 0:
            self.matrix[x][y] = mark
            return True
        else:
            return False

    def is_board_full(self):

        for x in xrange(0, self.board_width):
            for y in xrange(0, self.board_height):
                if self.matrix[x][y] == 0:
                    return False
        return True

    def get_winner(self):

        if (self.matrix[0][0] == self.matrix[1][0] == self.matrix[2][0] == 1) or \
                (self.matrix[0][1] == self.matrix[1][1] == self.matrix[2][1] == 1) or \
                (self.matrix[0][2] == self.matrix[1][2] == self.matrix[2][2] == 1) or \
                (self.matrix[0][0] == self.matrix[0][1] == self.matrix[0][2] == 1) or \
                (self.matrix[1][0] == self.matrix[1][1] == self.matrix[1][2] == 1) or \
                (self.matrix[2][0] == self.matrix[2][1] == self.matrix[2][2] == 1) or \
                (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == 1) or \
                (self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == 1):
            return 1

        if (self.matrix[0][0] == self.matrix[1][0] == self.matrix[2][0] == 2) or \
                (self.matrix[0][1] == self.matrix[1][1] == self.matrix[2][1] == 2) or \
                (self.matrix[0][2] == self.matrix[1][2] == self.matrix[2][2] == 2) or \
                (self.matrix[0][0] == self.matrix[0][1] == self.matrix[0][2] == 2) or \
                (self.matrix[1][0] == self.matrix[1][1] == self.matrix[1][2] == 2) or \
                (self.matrix[2][0] == self.matrix[2][1] == self.matrix[2][2] == 2) or \
                (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == 2) or \
                (self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == 2):
            return 2

        else:
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
