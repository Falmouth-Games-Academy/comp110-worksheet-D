class OxoBoard:
    board_rows = 3
    board_columns = 3
    board_array = []
    current_square = 0

    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """

        for x in range(self.board_rows):
            self.board_array.append([])

            for y in range(self.board_columns):
                self.board_array[x].append(0)

        print(self.board_array)
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
            self.current_square = mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        full_columns = 0
        for x in range(self.board_rows):
            if 0 in self.board_array[x]:
                return False
            else:
                full_columns += 1
        if full_columns == self.board_rows:
            return True

    def check_horizontal(self):
        player1_score = 0
        player2_score = 0
        for x in range(self.board_rows):
            for y in range(self.board_columns):

                if self.current_square == 1:
                    if 1 == self.board_array[y][x]:
                        player1_score += 1
                        if player1_score == 3:
                            return 1
                    else:
                        player1_score = 0

                elif self.current_square == 2:
                    if 2 == self.board_array[y][x]:
                        player2_score += 1
                        if player2_score == 3:
                            return 2
                    else:
                        player2_score = 0

        return 0

    def check_diagonal(self):
        x = int((self.board_rows-1) * 0.5)
        if self.current_square == 1:
            if 1 == self.board_array[x][x]\
                    == self.board_array[x - 1][0]\
                    == self.board_array[x + 1][2] \
                    or 1 == self.board_array[x][x]\
                    == self.board_array[x - 1][2]\
                    == self.board_array[x + 1][0]:
                    return 1
            else:
                return 0

        elif self.current_square == 2:
            if 2 == self.board_array[x][x]\
                    == self.board_array[x - 1][0]\
                    == self.board_array[x + 1][2] \
                    or 2 == self.board_array[x][x]\
                    == self.board_array[x - 1][2]\
                    == self.board_array[x + 1][0]:
                    return 2
            else:
                return 0
        else:
            return 0

    def check_vertical(self):
        for x in range(self.board_rows):
            if 0 not in self.board_array[x] and 2 not in self.board_array[x]:
                return 1
            if 0 not in self.board_array[x] and 1 not in self.board_array[x]:
                return 2
        return 0

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """

        diagonal = self.check_diagonal()
        vertical = self.check_vertical()
        horizontal = self.check_horizontal()
        print(self.board_array)
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
