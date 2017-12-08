
import random
"""This code is incomplete, and as predicted in the assignment brief, I had particular difficulty with the get_winner 
function. My original approach was to populate the game grid with a list of int. (0 to 8 for each square) and then only 
allow these squares to be appended with the characters 'x' and 'o', via the raw_input function. But this approach did 
not match the assignment brief, so I changed to the version below. I am more than happy to re-submit this assignment 
after Christmas, as i'm not particularly happy with what I have produced. I think this assignment clearly shows there 
are many areas where my knowledge of programming is completely absent. This I intend to rectify."""

class OxoBoard:
    grid_width = self.grith_width
    grid_height = self.grid_height
    winning_length = self.winning_length

    def __init__(self, grid_width, grid_height, winning_length):
        self.grid_width = 3
        self.grid_height = 3
        self.winning_length = 3

        self.board = [[0 for x in xrange(0, self.grid_width)]for y in xrange(0, self.grid_height)]

        self.show()


    def get_square(self, x, y):
        return self.board[x][y]


    def set_square(self, x, y):

       if self.board[x][y] == 0:
          self.board[x][y] = mark
          return True
       else:
           return False


    def set_square(self, x, y, mark):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """

        for x in xrange(0, self.grid_width):
            for y in xrange(0, self.grid_height):
                if self.board[x][y ] == 0:
                    board_state = False
                    break
        return board_state


    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
    while True


        raise NotImplementedError("TODO: implement get_winner")

    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """


                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print
