class OxoBoard:

    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        self.tiles_on_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.PLAYER_CROSS = 1
        self.PLAYER_NAUGHT = 2
        self.amount_for_win = 3

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.tiles_on_board[x][y]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.tiles_on_board[x][y] is 0:
            self.tiles_on_board[x][y] = mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        for x in range(len(self.tiles_on_board)):
            for y in range(len(self.tiles_on_board)):
                if self.tiles_on_board[x][y] is 0:
                    return False
        return True

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        for player in range(1, 3):
            diagonal_a = self.tiles_on_board[0][0] is player and self.tiles_on_board[1][1] is player\
                and self.tiles_on_board[2][2] is player
            diagonal_b = self.tiles_on_board[0][2] is player and self.tiles_on_board[1][1] is player\
                and self.tiles_on_board[2][0] is player
            if diagonal_a or diagonal_b:
                return player
            for i in range(len(self.tiles_on_board)):
                horizontal = self.tiles_on_board[i][0] is player and\
                    self.tiles_on_board[i][1] is player and self.tiles_on_board[i][2] is player
                vertical = self.tiles_on_board[0][i] is player and\
                    self.tiles_on_board[1][i] is player and self.tiles_on_board[2][i] is player
                if horizontal or vertical:
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
