class OxoBoard:
    board_rows = 0
    board_columns = 0
    board_array = []
    current_square = 0

    def __init__(self, size):
        """ The initialiser. Initialise any fields you need here. """

        self.board_rows = size
        self.board_columns = size
        # create the board array
        for x in range(self.board_rows):
            self.board_array.append([])

            for y in range(self.board_columns):
                self.board_array[x].append(0)

        self.show()

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """

        square_content = self.board_array[x][y]
        return square_content

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """

        if self.board_array[x][y] == 0:
            self.board_array[x][y] = mark
            # save the current squares' player mark
            self.current_square = mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """

        full_columns = 0

        # check if all of the columns are full
        for x in range(self.board_rows):
            if 0 in self.board_array[x]:
                return False
            else:
                full_columns += 1
        if full_columns == self.board_rows:
            return True

    def check_horizontal(self):
        """Check if a player has three in a row horizontally."""

        player1_score = 0
        player2_score = 0
        for x in range(self.board_rows):
            for y in range(self.board_columns):

                # check for player 1
                if self.current_square == 1:
                    if 1 == self.board_array[y][x]:
                        player1_score += 1
                        if player1_score == self.board_columns:
                            return 1
                    else:
                        player1_score = 0

                # check for player 2
                elif self.current_square == 2:
                    if 2 == self.board_array[y][x]:
                        player2_score += 1
                        if player2_score == self.board_columns:
                            return 2
                    else:
                        player2_score = 0

        return 0

    def check_diagonal(self):
        """Check if a player has three in a row diagonally."""

        connected_o_1 = 0
        connected_x_1 = 0

        # check first diagonal line
        for y in range(self.board_columns - 1, -1, -1):

            # check for player 1
            if self.board_array[y][y] == 1:
                connected_o_1 += 1
            else:
                connected_o_1 = 0
            if connected_o_1 == self.board_columns:
                return 1

            # check for player 2
            if self.board_array[y][y] == 2:
                connected_x_1 += 1
            else:
                connected_x_1 = 0
            if connected_x_1 == self.board_columns:
                return 2

        connected_o_2 = 0
        connected_x_2 = 0
        x = -1

        # check second diagonal line
        for y in range(self.board_columns - 1, -1, -1):
            x += 1

            # check for player 1
            if self.board_array[x][y] == 1:
                connected_o_2 += 1
            else:
                connected_o_2 = 0
            if connected_o_2 == self.board_columns:
                return 1

            # check for player 2
            if self.board_array[x][y] == 2:
                connected_x_2 += 1
            else:
                connected_x_2 = 0
            if connected_x_2 == self.board_columns:
                return 2

        return 0

    def check_vertical(self):
        """Check if a player has three in a row vertically."""

        for x in range(self.board_rows):

            # check for player 1
            if 0 not in self.board_array[x] and 2 not in self.board_array[x]:
                return 1

            # check for player 2
            if 0 not in self.board_array[x] and 1 not in self.board_array[x]:
                return 2

        return 0

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """

        # get results
        diagonal = self.check_diagonal()
        vertical = self.check_vertical()
        horizontal = self.check_horizontal()

        # compare all results
        if diagonal == 0:
            if vertical == 1 \
                    or horizontal == 1:
                return 1
            elif vertical == 2 \
                    or horizontal == 2:
                return 2
            else:
                return 0
        else:
            return diagonal

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
