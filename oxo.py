class OxoBoard:
    def __init__(self):
        """ The initialiser. Initialise any fields you need here."""
        # nested list of square contents
        self.squares = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square."""
        return self.squares[y][x]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.squares[y][x] == 0:
            self.squares[y][x] = mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True."""
        if 0 in [elem for sublist in self.squares for elem in sublist]:
            print('not full')
            return False

        else:
            print('full')
            return True

    def get_winner(self, player):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0."""
        '''
        for i in range(0, len(self.squares)):  # check vertically
            if self.squares[0][i] == \
                    self.squares[0][i] == \
                    self.squares[0][i] and self.squares[0][i] != 0:
                print('Vertical win')
                return player
        for i in range(0, len(self.squares)):  # check vertically
            if self.squares[i][0] == \
                    self.squares[i][1] == \
                    self.squares[i][2] and self.squares[i][0] != 0:
                print('Horizontal win')
                return player
        print('none')
        return 0
        '''

        for i in range(0, len(self.squares)):  # check vertically
            if self.squares[0][i] == \
                    self.squares[1][i] == \
                    self.squares[2][i] != 0:
                print('Vertical win')
                return player
            elif self.squares[i][0] == \
                    self.squares[i][1] == \
                    self.squares[i][2] != 0:
                print('Horizontal win')
                return player
            else:
                return 0

            # TODO: implement diagonal win

    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this."""
        for y in range(3):
            if y > 0:
                print("--+---+--")
            for x in range(3):
                if x > 0:
                    print('|',)

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print(" OX"[self.get_square(x, y)],)
            print
