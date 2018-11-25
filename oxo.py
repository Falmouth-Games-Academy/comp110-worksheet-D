class OxoBoard:

    PLAYER_y = 0
    PLAYER_X = 1

    def __init__(self, grid_width=3, grid_height=3, win_row_amount=3):
        """ The initialiser. Initialise any fields you need here.

        :param board_width:     width of board
        :param board_height:    height of board
        :param win_row_amount:
        """
        self.grid_size = {"width": grid_width, "height": grid_height}
        self.total_cells = grid_width * grid_height
        self.grid = {}
        self.win_row_amount = win_row_amount

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        if (x, y) in self.grid:
            return self.grid[(x, y)]
        else:
            return 0

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if (x, y) not in self.grid:
            self.grid[(x, y)] = mark
            return True
        else:
            return False


    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        return len(self.grid) == self.total_cells

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        for player_index in range(1, 3, 1):
            winner = self.check_hoz(player_index)
            if winner != 0:
                return winner
            winner = self.check_vert(player_index)
            if winner != 0:
                return winner
            winner = self.check_diagonals(player_index)
            if winner != 0:
                return winner
        return 0

    def check_hoz(self, player):
        """Check the horizontally for a winner

        :param player:  player index
        :return:        winner id (0 if no winner)
        """
        # there is no point checking the board if the grid is not wide enough for the win condition
        if self.win_row_amount > self.grid_size["width"]:
            return 0

        count_in_row = 0

        for y in range(self.grid_size["height"]):
            for x in range(self.grid_size["width"]):

                # break if its not possible to get the required amount it a row
                if count_in_row == 0 and self.grid_size["width"] - x < self.win_row_amount:
                    break;

                # reset and continue if we have no input
                if (x, y) not in self.grid:
                    count_in_row = 0
                    continue

                if self.grid[(x, y)] == player:
                    count_in_row += 1
                else:
                    count_in_row = 0

                if count_in_row == self.win_row_amount:
                    return player

            count_in_row = 0

        return 0

    def check_vert(self, player):
        """Check the vertically for a winner

        :param player:  player index
        :return:        winner id (0 if no winner)
        """
        # there is no point checking the board if the grid is not wide enough for the win condition
        if self.win_row_amount > self.grid_size["height"]:
            return 0

        count_in_row = 0

        for x in range(self.grid_size["width"]):
            for y in range(self.grid_size["height"]):

                # break if its not possible to get the required amount it a row
                if count_in_row == 0 and self.grid_size["height"] - y < self.win_row_amount:
                    break;

                # reset and continue if we have no input
                if (x, y) not in self.grid:
                    count_in_row = 0
                    continue

                if self.grid[(x, y)] == player:
                    count_in_row += 1
                else:
                    count_in_row = 0

                if count_in_row == self.win_row_amount:
                    return player

            count_in_row = 0

        return 0

    def check_diagonals(self, player):
        """Check both diagonals (left to right and right to left) for a winner

        :param player:  player index
        :return:        winner id (0 if no winner)
        """
        for x in range(self.grid_size["width"]):
            for y in range(self.grid_size["height"]):
                # check diagonal left to right
                winner = self.check_diagonal(x, y, player, True)
                if winner != 0:
                    return winner

                # check diagonal right to left
                winner = self.check_diagonal(x, y, player, False)
                if winner != 0:
                    return winner

        return 0

    def check_diagonal(self, start_x, start_y, player, left_to_right):
        """ Check for a winner on the diagonal from start x and start y

        :param start_x:         start x position
        :param start_y:         start y position
        :param player:          player index
        :param left_to_right:   Should it check from left to right (true)
                                or right to left (false)
        :return:                winner id (0 if no winner)
        """
        # check that there is an input for player to start with.
        if (start_x, start_y) not in self.grid:
            return 0
        elif self.grid[(start_x, start_y)] != player:
            return 0


        count_in_row = 0

        for i in range(self.win_row_amount):

            offset_x = i
            offset_y = i
            # invert x offset if checking right to left
            if not left_to_right:
                offset_x = -i

            x, y = start_x + offset_x, start_y + offset_y

            # return if x goes less than 0 (can not be a winner)
            if x < 0:
                return 0

            # if there is no input or player don't match return (can not win)
            if (x, y) not in self.grid:
                return 0
            elif self.grid[(x, y)] != player:
                return 0
            else:
                count_in_row += 1

            if count_in_row == self.win_row_amount:
                return player

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
