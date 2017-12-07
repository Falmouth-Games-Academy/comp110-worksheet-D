class OxoBoard:
    """
    Game board class.

    Attributes:
        board (list of list of int): The gameboard.
        player (int): The player who is currently playing.
        winning_boards (list of list of int): The possible winning board states. Note that the numbers represent the
                                              player's positions in the board as 0 - 8 (top to bottom, left to right).
    """

    board = []
    player = 0

    winning_boards = [
                      # Horizontal wins
                      [0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8],

                      # Vertical wins
                      [0, 3, 6],
                      [1, 4, 7],
                      [2, 5, 8],

                      # Diagonal wins
                      [0, 4, 8],
                      [6, 4, 2]
                     ]

    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """

        # Board is so small it's simpler to manually declare it.
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def get_square(self, x, y):
        """
        Return 0, 1 or 2 depending on the contents of the specified square.

        Args:
            x (int): The x position of the square.
            y (int): The y position of the square.

        Returns:
            int: The value of the game board at position x, y.
        """

        return self.board[x][y]

        # raise NotImplementedError("TODO: implement get_square")

    def set_square(self, x, y, mark):
        """
        If the specified square is currently empty (0), fill it with mark and return True.
        If the square is not empty, leave it as-is and return False.

        Args:
            x (int): x position to place mark.
            y (int): y position to place mark.
            mark (int): The player's mark to place.

        Return:
            bool: True if square is empty and mark is placed. False if square is filled already.
        """

        if self.board[x][y] == 0:
            self.board[x][y] = mark
            self.player = mark
            return True
        else:
            return False

    def is_board_full(self):
        """
        If there are still empty squares on the board, return False.
        If there are no empty squares, return True.

        Returns:
            bool: False is board is not yet full. True if board is full.
        """

        for x in self.board[0]:
            for y in self.board[1]:
                if self.board[x][y] == 0:
                    return False

        return True

    def collect_positions(self, player):
        """Collects all the positions owned by a player

        Args:
            player (int): The player to check positions of.

        Returns:
            played_spaces (list of int): A list of the spaces owned by the specified player in the format: 0, 1...8 (Right to left, top to bottom).
        """

        played_spaces = []

        for x in range(0, 3):
            for y in range(0, 3):
                if self.board[x][y] == player:
                    position = [x, y]

                    played_spaces.append(self.convert_to_1d_index(position, 3))

        return played_spaces

    def convert_to_1d_index(self, index, height):
        """
        Convert the indexes of a 2d array into a single index for a 1d array. Used to convert the x, y of board space into a single position.

        Args:
            index (list of int): The x, y indexes stored in a list.
            height (int): The y dimension of the 2d array.

        Returns:
            new_index (int): The new index for a 1d array.
        """

        x = index[0]
        y = index[1]

        new_index = x + (y * height)
        return new_index

    def compare_lists(self, master_list, list_to_compare):
        """
        Check to see if a master list contains all the same items as the list being compared.

        Args:
            master_list (list): The main list.
            list_to_compare (list): The list to compare to master.

        Returns:
            (bool): The result of a set comparison. True if master_list contains all elements in list_to_compare.
        """

        return set(list_to_compare) <= set(master_list)

    def evaluate_board(self, player):
        """
        Evaluates the game board to see how many wins a given player has.

        Args:
            player (int); The player to evaluate for.

        Returns:
            number_of_wins (int): The number of wins the player has.
        """

        number_of_wins = 0
        played_spaces = self.collect_positions(player)

        for i in range (0, 8):
            if self.compare_lists(played_spaces, self.winning_boards[i]) == True:
                number_of_wins += 1

        return number_of_wins

    def get_winner(self):
        """
        If a player has three in a row, return 1 or 2 depending on which player.
        Otherwise, return 0.

        Returns:
            int: The winning player if one is found, otherwise 0.
        """

        if self.evaluate_board(self.player) >= 1:
            return self.player

        return 0

    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """

        for y in xrange(3):
            if y > 0:
                print "--+---+--"

            for x in xrange(3):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print
