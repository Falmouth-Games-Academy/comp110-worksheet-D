class OxoBoard:
    def __init__(self, custom_width=3, custom_height=3):
        """ The initialiser. Initialise any fields you need here. """

        self.board = {}
        self.width = custom_width
        self.height = custom_height

        for x in range(0, custom_width):
            for y in range(0, custom_height):
                self.board[x, y] = 0

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.board[x, y]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """

        if self.board[x, y] == 0:
            self.board[x, y] = mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """

        return False if 0 in self.board.values() else True

    def get_winner(self, row_length=3):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """

        for cell in self.board:

            if self.board[cell] != 0:

                # NOTE: DISPLAY IS FLIPPED DIAGONALLY (oof)

                # For each cell, we will search in 4 directions:

                # Horizontally (to the right)

                if cell[1] + row_length <= self.width:

                    for y in range(cell[1] + 1, cell[1] + row_length):

                        if self.board[cell[0], y] != self.board[cell]:
                            break
                        elif y == cell[1] + row_length - 1:
                            return self.board[cell]

                # Diagonally (top left to bottom right)

                if cell[1] + row_length <= self.width \
                        and cell[0] + row_length <= self.height:

                    y = cell[1] + 1

                    for x in range(cell[0] + 1, cell[0] + row_length):

                        if self.board[x, y] != self.board[cell]:
                            break
                        elif x == cell[0] + row_length - 1:
                            return self.board[cell]
                        y += 1

                # Diagonally (bottom left to top right)

                if cell[1] + row_length <= self.width \
                        and cell[0] - row_length + 1 >= 0:

                    y = cell[1]

                    for x in range(cell[0] - 1, cell[0] - row_length, -1):

                        y += 1

                        if self.board[x, y] != self.board[cell]:
                            break
                        elif x == cell[0] - row_length + 1:
                            return self.board[cell]

                # Vertically (downwards)

                if cell[0] + row_length <= self.height:

                    for x in range(cell[0] + 1, cell[0] + row_length):

                        if self.board[x, cell[1]] != self.board[cell]:
                            break
                        elif x == cell[0] + row_length - 1:
                            return self.board[cell]

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
