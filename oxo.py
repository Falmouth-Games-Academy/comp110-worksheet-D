class OxoBoard:

    def __init__(self):
        """ The initialiser. Initialise any fields you need here."""

        # nested list of square contents
        self.squares = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

        self.current_player = 1

    def get_square(self, x, y):
        """
        _______________________________________________________________________
        Return 0, 1 or 2 depending on the contents of the specified square.
        :param x: grid x position
        :param y: grid y position
        :return: current contents of grid at specified position
        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        """

        return self.squares[y][x]

    def set_square(self, x, y, player):
        """
        _______________________________________________________________________
         If the specified square is currently empty (0), fill it with mark and
         return True. Otherwise , leave it as-is and return False.
        :param x: grid x position
        :param y: grid y position
        :param player: current player, also used for setting the
                                    square's contents (0, 1, or 2)
        :return: True or False depending on whether square is full
        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        """
        self.current_player = player

        if self.squares[y][x] == 0:
            self.squares[y][x] = player
            return True
        else:
            return False

    def is_board_full(self):
        """
        _______________________________________________________________________
        If there are still empty squares on the board, return False.
            If there are no empty squares, return True.
        :return: True or False depending on whether all squares are full
        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        """

        if 0 in [items for sublist in self.squares for items in sublist]:
            return False

        else:
            return True

    def get_winner(self):
        """
        _______________________________________________________________________
        If a player has three in a row, return 1 or 2 depending on which
        player. Otherwise, return 0.
        :param player: current player (1 or 2)
        :return: winning player (0 if no win this turn)
        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        """

        for i in range(0, len(self.squares)):
            # check horizontal win
            if self.squares[i][0] == \
                    self.squares[i][1] == \
                    self.squares[i][2] != 0:
                return self.current_player
            # check vertical win
            elif self.squares[0][i] == \
                    self.squares[1][i] == \
                    self.squares[2][i] != 0:
                return self.current_player
            # check diagonal win
            elif self.squares[0][i-2] == \
                    self.squares[1][i-1] == \
                    self.squares[2][i] != 0:
                return self.current_player
            # check diagonal win
            elif self.squares[0][i] == \
                    self.squares[1][i-1] == \
                    self.squares[2][i-2] != 0:
                return self.current_player

        return 0

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
