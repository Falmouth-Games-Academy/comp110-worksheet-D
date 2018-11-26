class OxoBoard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        board_list = []
        for i in range(self.x):
            for j in range(self.y):
                board_list.append([(i, j), [0]])
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
                index = i
                self.board_list[index][1] = mark
                return True
        return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        for i in range(len(self.board_list)):
            current_position = self.board_list[i][1]
            if current_position == [0]:
                return False
        return True

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        player_one_counter = 0
        player_two_counter = 0
        for i in range(0, 2, 3):
            if i == 1:
                if [1] in (self.board_list[i][1] and self.board_list[i + 4][1] and self.board_list[i + 8][1]):
                    return 1
                elif [2] in (self.board_list[i][1] and self.board_list[i + 4][1] and self.board_list[i + 8][1]):
                    return 2
            elif i == 3:
                if [1] in (self.board_list[i][1] and self.board_list[i + 2][1] and self.board_list[i + 4][1]):
                    return 1
                elif [2] in (self.board_list[i][1] and self.board_list[i + 2][1] and self.board_list[i + 4][1]):
                    return 2
            for j in range(0, 2):
                # horizontal check
                if self.board_list[i - j][1] == 1:
                    player_one_counter += 1
                elif self.board_list[i - j][1] == 2:
                    player_two_counter += 1
                if player_one_counter == 3:
                    return 1
                elif player_two_counter == 3:
                    return 2
                else:
                    player_one_counter, player_two_counter = 0, 0
                # vertical check
                if [1] in (self.board_list[i - j] and self.board_list[i - j + 3] and self.board_list[i - j + 6]):
                    return 1
                elif [2] in (self.board_list[i - j] and self.board_list[i - j + 3] and self.board_list[i - j + 6]):
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
