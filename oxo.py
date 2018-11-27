class OxoBoard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        board_list = []
        for i in range(self.x):
            for j in range(self.y):
                board_list.append([(i, j), 0])
        print(board_list)
        self.board_list = board_list
        """ The initialiser. Initialise any fields you need here. """

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        for i in range(len(self.board_list)):
            if self.board_list[i][0] == (x, y):
                index = i
                if self.board_list[index][1] == 0:
                    return 0
                elif self.board_list[index][1] == 1:
                    return 1
                elif self.board_list[index][1] == 2:
                    return 2

    def set_square(self, x, y, mark):
        for i in range(len(self.board_list)):
            if self.board_list[i][0] == (x, y):
                if self.board_list[i][1] == 0:
                    self.board_list[i][1] = mark
                    return True
                else:
                    return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        for i in range(len(self.board_list)):
            if self.board_list[i][1] == 0:
                return False
        return True

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0.
            This is not very maintainable and will not work for the possibility of having a larger grid
        """
        print(self.board_list)
        # Horizontal checking
        for x in range(0, 2):
            if 1 in [self.board_list[x][1]] and 1 in [self.board_list[x + 3][1]] and 1 in [self.board_list[x + 6][1]]:
                return 1
            elif 2 in [self.board_list[x][1]] and 2 in [self.board_list[x + 3][1]] and 2 in [self.board_list[x + 6][x]]:
                return 2
        # Vertical checking
        for y in range(0, 8, 3):
            if 1 in [self.board_list[y - 2][1]] and 1 in [self.board_list[y - 1][1]] and 1 in [self.board_list[y-1][1]]:
                return 1
            if 2 in [self.board_list[y - 2][1]] and 2 in [self.board_list[y - 1][1]] and 2 in [self.board_list[y][1]]:
                return 2
        # Diagonal Checking
        if 1 in [self.board_list[0][1]] and 1 in [self.board_list[4][1]] and 1 in [self.board_list[8][1]]:
            return 1
        if 2 in [self.board_list[0][1]] and 2 in [self.board_list[4][1]] and 2 in [self.board_list[8][1]]:
            return 2
        if 1 in [self.board_list[2][1]] and 1 in [self.board_list[4][1]] and 1 in [self.board_list[6][1]]:
            return 1
        if 2 in [self.board_list[2][1]] and 2 in [self.board_list[4][1]] and 2 in [self.board_list[6][1]]:

            return 2

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
