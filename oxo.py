class OxoBoard:

    # The gameboard state
    board = []
    player = 0

    # <editor-fold desc="Win conditions for player 1 (wins1)">

    # Possible wins
    wins1 = [[[1, 1, 1],
              [0, 0, 0],
              [0, 0, 0]],

             [[0, 0, 0],
              [1, 1, 1],
              [0, 0, 0]],

             [[0, 0, 0],
              [0, 0, 0],
              [1, 1, 1]],

             [[1, 0, 0],
              [1, 0, 0],
              [1, 0, 0]],

             [[0, 1, 0],
              [0, 1, 0],
              [0, 1, 0]],

             [[0, 0, 1],
              [0, 0, 1],
              [0, 0, 1]],

             [[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]],

             [[0, 0, 1],
              [0, 1, 0],
              [1, 0, 0]]]
    # </editor-fold>

    # <editor-fold desc="Win conditions for player 2 (wins2)">

    # Possible wins
    wins2 = [[[2, 2, 2],
             [0, 0, 0],
             [0, 0, 0]],

            [[0, 0, 0],
             [2, 2, 2],
             [0, 0, 0]],

            [[0, 0, 0],
             [0, 0, 0],
             [2, 2, 2]],

            [[2, 0, 0],
             [2, 0, 0],
             [2, 0, 0]],

            [[0, 2, 0],
             [0, 2, 0],
             [0, 2, 0]],

            [[0, 0, 2],
             [0, 0, 2],
             [0, 0, 2]],

            [[2, 0, 0],
             [0, 2, 0],
             [0, 0, 2]],

            [[0, 0, 2],
             [0, 2, 0],
             [2, 0, 0]]]
    # </editor-fold>

    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """

        # Board is so small its simpler to manually declare it
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def get_square(self, x, y):
        """
        Return 0, 1 or 2 depending on the contents of the specified square.
        """

        return self.board[x][y]

        # raise NotImplementedError("TODO: implement get_square")

    def set_square(self, x, y, mark):
        """
        If the specified square is currently empty (0), fill it with mark and return True.
        If the square is not empty, leave it as-is and return False.
        """

        # TODO Check how x and y are passed. If the are 1-3 instead of 0-2, subtract 1 from x and y.
       #x = 3 - x
        #y = 3 - y

        if self.board[x][y] == 0:
            self.board[x][y] = mark
            self.player = mark
            return True
        else:
            return False

    def is_board_full(self):
        """
        If there are still empty squares on the board, return False.
        If there are no empty squares, return True.
        """

        for x in self.board[0]:
            for y in self.board[1]:
                if self.board[x][y] == 0:
                    return False

        #raise NotImplementedError("TODO: implement is_board_full")

    def check_lines(self, x, y):

        for x in range(x, ):
            pass

    def get_winner(self):
        """
        If a player has three in a row, return 1 or 2 depending on which player.
        Otherwise, return 0.
        """
        print("Player being checked = " + str(self.player))
        print(str(self.board[0]) + "\n" + str(self.board[1]) + "\n" + str(self.board[2]))

        # returns false because 0's are not 0's!!!!

        if self.player == 1:
            for i in range(0, 8):
                print("Checking win no. " + str(i))

                # print(str(self.wins1[0]) + "\n" + str(self.wins1[1]) + "\n" + str(self.wins1[2]))
                if self.board == self.wins1[i]:
                    return 1

        elif self.player == 2:
            for i in range(0, 8):
                print("Checking win no. " + str(i))

                # print(str(self.wins2[0]) + "\n" + str(self.wins2[1]) + "\n" + str(self.wins2[2]))
                if self.board == self.wins2[i]:
                    return 2

        else:
            print("Player not set correctly.")


        return 0
        # raise NotImplementedError("TODO: implement get_winner")




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

"""

test_board = OxoBoard()

test_board.set_square(0, 0, 2)
test_board.set_square(1, 0, 2)
test_board.set_square(2, 0, 2)

print(str(test_board.wins1[3]))

# Print out board
print(str(test_board.board[0]) + "\n" + str(test_board.board[1]) + "\n" + str(test_board.board[2]))

print("winner is player " + str(test_board.get_winner()))



# print(str(zip(test_board.board, test_board.wins[0])[0]))

# print(str(test_board.get_winner()))


# print(str(test_board.is_board_full()))
# print(str(test_board.get_square(1, 1)))
"""


