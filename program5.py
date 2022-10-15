import numpy as np
import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 5: DigiPeg Solitaire          |
# Your Name(, Your Partner's Name)      |
# Last Modified: ??, 2020               |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

# ---------------------------------------
# Start of DigiPeg Class                |
# ---------------------------------------

class DigiPeg:

    def __init__(self, rows, columns, empty_row, empty_col):
        self.board = np.full((rows, columns), True)
        self.board[empty_row][empty_col] = False
        self.pegs_left = rows * columns - 1
        
# ---------------------------------------

    def __str__(self):
        answer = "   "
        for column in range(self.board.shape[1]):
            answer += " " + str(column + 1) + "  "
        answer += "\n"
        answer += self.separator()
        for row in range(self.board.shape[0]):
            answer += str(row + 1) + " |"
            for col in range(self.board.shape[1]):
                if self.board[row][col]:
                    answer += " o |"
                else:
                    answer += "   |"
                    print("This space is empty", row, col)
                    if (row-2 in range(self.board.shape[0])) and (col-1 in range(self.board.shape[1])):
                        print("This is the row-2 and col-1", self.board[row-2][col-1])
            answer += "\n" 
            answer += self.separator()
        return answer
    
# ---------------------------------------

    def separator(self):
        answer = "  +"
        for _ in range(self.board.shape[1]):
            answer += "---+"
        answer += "\n"
        return answer

# ---------------------------------------
# The four missing methods go here.  Do |
# not modify anything else.             |
# --------------------------------------|

    #def game_over(self):
        
        
        #pass

    def game_over(self):

        answer = True

        for columns in range(self.board.shape[1]):

            for rows in range(self.board.shape[0]):

                if (self.board[rows][columns] == False):    #above space open to the left

                    row = rows - 1

                    column = columns - 1

                    print("empty space at:", "(",rows+1,",", columns+1,")")

                    if (self.board[row][column] == True):

                        row -= 1

                        column -= 1

                        print("checking twice")

                        if (self.board[row][column] == True):

                            answer = False

                elif (self.board[rows][columns] == False):    #above space open

                    row = rows - 1

                    column = columns

                    if (self.board[row][column] == True):

                        row -= 1

                        if (self.board[row][column] == True):

                            answer = False

                elif (self.board[rows][columns] == False):    #above space to the right

                    row = rows - 1

                    column = columns + 1

                    if (self.board[row][column] == True):

                        row -= 1

                        column += 1

                        if (self.board[row][column] == True):

                            answer = False

                elif (self.board[rows][columns] == False):    #left of space open

                    row = rows

                    column = columns - 1

                    if (self.board[row][column] == True):

                        column -= 1

                        if (self.board[row][column] == True):

                            answer = False

                elif (self.board[rows][columns] == False):    #Left and below open space

                    row = rows + 1

                    column = columns - 1

                    if (self.board[row][column] == True):

                        row += 1

                        column -= 1

                        if (self.board[row][column] == True):

                            answer = False

                elif (self.board[rows][columns] == False):    #below open space

                    row = rows - 1

                    column = columns

                    if (self.board[row][column] == True):

                        row -= 1

                        if (self.board[row][column] == True):

                            answer = False

                elif (self.board[rows][columns] == False):    #Below and right of open space

                    row = rows - 1

                    column = columns + 1

                    if (self.board[row][column] == True):

                        row -= 1

                        column += 1

                        if (self.board[row][column] == True):

                            answer = False

                elif (self.board[rows][columns] == False):    #to the right of open space

                    row = rows

                    column = columns + 1

                    if (self.board[row][column] == True):

                        column += 1

                        if (self.board[row][column] == True):

                            answer = False

        return answer



    def final_message(self):

        counter = 0 

        for columns in range(self.board.shape[1]):

            for rows in range(self.board.shape[0]):

                if (self.board[rows][columns] == True):

                    counter += 1

        if (counter <= 2):

            print("You're a DigiPeg-enius!")

        elif (counter == 3 or counter == 4):

            print("I've worked with better. But not many.")

        elif (counter == 5 or counter == 6):

            print(counter,"left? Really? You're gonna have to do better than that.")

        elif (counter >= 7):

            print("DigiPeg-naramous! Rack 'em up and redeem youseslf.")

            



    def legal_move(self, rstart, cstart, rend, cend):

        a = False

        if ((self.board[rstart][cstart] == True) and (self.board[rend][cend] == False)):

            if ((self.board[rstart][cstart+1] == True) and (self.board[rstart][cstart+2] == False)):

                if((rend == rstart) and (cend == cstart+2)):

                    a = True

            elif ((self.board[rstart][cstart-1] == True) and (self.board[rstart][cstart-2] == False)):

                if((rend == rstart) and (cend == cstart-2)):

                    a = True

            elif ((self.board[rstart-1][cstart] == True) and (self.board[rstart-2][cstart] == False)):

                if((rend == rstart-2) and (cend == cstart)):

                    a = True

            elif ((self.board[rstart+1][cstart] == True) and (self.board[rstart+2][cstart] == False)):

                if((rend == rstart+2) and (cend == cstart)):

                    a = True

            elif ((self.board[rstart+1][cstart-1] == True) and (self.board[rstart+2][cstart-2] == False)):

                if((rend == rstart+2) and (cend == cstart-2)):

                    a = True

            elif ((self.board[rstart+1][cstart+1] == True) and (self.board[rstart+2][cstart+2] == False)):

                if((rend == rstart+2) and (cend == cstart+2)):

                    a = True

            elif ((self.board[rstart-1][cstart+1] == True) and (self.board[rstart-2][cstart+2] == False)):

                if((rend == rstart-2) and (cend == cstart+2)):

                    a = True

            elif ((self.board[rstart-1][cstart-1] == True) and (self.board[rstart-2][cstart-2] == False)):

                if((rend == rstart-2) and (cend == cend-2)):

                    a = True



        return a

    

    def make_move(row_start, col_start, row_end, col_end):

        self.board[rstart][cstart] = False

        self.board[rend][cend] = True

        if (rstart-2 == rend) and (cstart-2 == cend): #2 left and 2 above

            self.board[rstart-1][cstart-1] = False

        elif (rstart-2 == rend) and (cstart == cend): #2 above

            self.board[rstart-1][cstart] = False

        elif (rstart-2 == rend) and (cstart+2 == cend): #2 right and 2 above

            self.board[rstart-1][cstart+1] = False

        elif (rstart == rend) and (cstart-2 == cend): #2 right

            self.board[rstart][cstart-1] = False

        elif (rstart+2 == rend) and (cstart-2 == cend): #2 left and 2 below

            self.board[rstart-1][cstart-1] = False

        elif (rstart-2 == rend) and (cstart == cend): #2 below

            self.board[rstart-1][cstart] = False

        elif (rstart+2 == rend) and (cstart+2 == cend): #2 right and 2 below

            self.board[rstart+1][cstart+1] = False

        elif (rstart == rend) and (cstart+2 == cend): #2 right

            self.board[rstart][cstart+1] = False
            
        

# ---------------------------------------
# End of DigiPeg Class               |
# ---------------------------------------

def get_choice(low, high, message):
    message += " [" + str(low) + " - " + str(high) + "]: "
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    print("Welcome to DigiPeg Solitaire!")
    print("-----------------------------------\n")
    
    rows = get_choice(1, 9, "Enter the number of rows")
    columns = get_choice(1, 9, "Enter the number of columns")
    row = get_choice(1, rows, "Enter the empty space row") - 1
    column = get_choice(1, columns, "Enter empty space column") - 1   
    game = DigiPeg(rows, columns, row, column)
    print()

    print(game)
    while (not game.game_over()):
        row_start = get_choice(1, rows, "Enter the row of the peg to move") - 1
        col_start = get_choice(1, columns, "Enter the column of the peg to move") - 1
        row_end = get_choice(1, rows, "Enter the row where the peg lands") - 1
        col_end = get_choice(1, columns, "Enter the column where the peg lands") - 1
        if game.legal_move(row_start, col_start, row_end, col_end):
            game.make_move(row_start, col_start, row_end, col_end)
        else:
            print("Sorry.  That move is not allowed.")
        print()
        print(game)

    game.final_message()

# ---------------------------------------

main()
