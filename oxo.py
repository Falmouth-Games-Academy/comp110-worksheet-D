class OxoBoard:

    def __init__(self, grid_width, grid_height, win_length):
        self.grid_width = grid_width  # Stores number of columns in class
        self.grid_height = grid_height  # Stores number of rows in class
        self.win_length = win_length  # Stores win_length in class
        self.board = [[0 for x in xrange(0, grid_width)] for y in xrange(0, grid_height)]
        # Sets a list to hold the board state
        self.show()

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.board[x][y]  # Returns board state at x,y

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.board[x][y] == 0:
            self.board[x][y] = mark  # Sets current square to the given mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        board_state = True  # Changed to False if the board in not full
        for x in xrange(0, self.grid_width):  # Loops check every square on the board
            for y in xrange(0, self.grid_height):
                if self.board[x][y] == 0:
                    board_state = False  # If a square is empty change board_state
                    break
        return board_state

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. This function was inspired by Louis as I was a bit stuck"""
        check_direction = [(1, 0), (1, 1), (1, -1), (0, 1)]  # Used to check right, down right, up right, and down
        for x in xrange(0, self.grid_width):
            for y in xrange(0, self.grid_height):
                current_item = self.board[x][y]  # Item on the board we will be checking if the others match

                if current_item == 0:  # If empty move on to the next square
                    continue

                for i in xrange(0, 4):  # For each given direction check to see if it matches,
                    # then continue in that direction until no match or matches = win_length
                    matches = 0  # Used to check number of matches resets when the check starts again
                    for p in xrange(1, self.win_length):
                        pos_x = x + check_direction[i][0] * p  # Gives x position moving relative to p
                        pos_y = y + check_direction[i][1] * p  # Gives y position moving relative to p
                        matches += 1  # Increases for each match

                        if pos_x < 0 or pos_y < 0 or pos_x >= self.grid_width or pos_y >= self.grid_height:
                            break  # Break if outside of the list range

                        if self.board[pos_x][pos_y] != current_item:
                            break  # Break if items don't match

                        if matches == self.win_length - 1:
                            # If enough items match in line to equal the win length return the winner
                            return current_item
        return 0  # If no winner return 0

    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in xrange(self.grid_height):
            if y > 0:
                print "--+" + "---+" * (self.grid_width - 2) + "--"
            for x in xrange(self.grid_width):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print


