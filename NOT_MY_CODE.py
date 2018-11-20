"""
def checkVictory():

    #This method looks at each box in the grid and checks the two boxes
    #in each of the four directions defined as vectors below

    for i in range(0, 3):
        for j in range(0, 3):

            if (boxes[i][j] == 0):
                continue

            for vector in [[1, 0], [1, 1], [0, 1], [-1, 1]]:
                # The four directions to check for a complete line in

                try:
                    boxToCheck = [i, j]
                    charToCheckFor = boxes[i][j]
                    for x in range(1, 3):

                        boxToCheck[0] += vector[0]
                        boxToCheck[1] += vector[1]

                        #Check if the box contains the same symbol as the previous ones in the line
                        if (boxes[boxToCheck[0]][boxToCheck[1]] != charToCheckFor):
                            break

                        #If we're on the last box in the loop and haven't broken out yet,
                        #we've found 3 in a row. Return the character in the box.
                        if (x == 2):
                            return intToText(boxes[i][j])

                except:
                    continue
    return ' '"""