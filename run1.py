import random
import sys

class GameBoard:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        """
        After each guess, print_board to the user
        """
        print("  1 2 3 4 5 6 7 8")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

class Battleship:
    def __init__(self, player_name, board):
        self.player_name = player_name
        self.board = board

    def create_ships(self):
        """
        Creates the ships
        """
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board
    
    def get_user_input(self):   
        """
        User input. The user guesses the row and the column
        """
        try:
            x_row = input("Guess a row: ")
            while x_row not in '12345678':
                print('Not an appropriate choice, please select a valid row')
                x_row = input("Guess a row:")

            y_column = input("Guess a column: ")
            while y_column not in "12345678":
                print('Not an appropriate choice, please select a valid column')
                y_column = input("Guess a column: ")
            return int(x_row) - 1, int(y_column) -1        #-1 as the list starts at 0
        except ValueError and KeyError:
            print("Not a valid input")
            return self.get_user_input()   
        

        
    def count_hit_ships(self):
        """
        Count the ships on the board
        """
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships

"""
Function to exit the game
"""
def exit_program():
    print("Exiting the program...")
    sys.exit(0)


def RunGame():
    computer_board = GameBoard([[" "] * 8 for i in range(8)])
    user_guess_board = GameBoard([[" "] * 8 for i in range(8)])
    Battleship.create_ships(computer_board)
    size = 7
    num_ships = 4
    print("Welcome to BATTLESHIPS!!")
    print(f"Board Size: {size}. Number of ships: {num_ships}")
    print(" Top left corner is row: 0, col 0")
    print("-" * 35)
    player_name = input("Please enter your name: \n")
    print("-" * 35)
    #start 10 turns
    turns = 10
    while turns > 0:
        GameBoard.print_board(user_guess_board)
        #get user input
        user_x_row, user_y_column = Battleship.get_user_input(object)
        #check if duplicate guess
        while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board.board[user_x_row][user_y_column] == "X":
            print(f"You guessed that one already {player_name}")
            user_x_row, user_y_column = Battleship.get_user_input(object)
        #check for hit or miss
        if computer_board.board[user_x_row][user_y_column] == "X":
            print(f"Well done {player_name}, You sunk 1 of my battleships!")
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print(f"You missed my battleship {player_name}!")
            user_guess_board.board[user_x_row][user_y_column] = "-"
        #check for win or lose
        if Battleship.count_hit_ships(user_guess_board) == 5:
            print(f"Well done {player_name}, You hit all battleships!")
            break
        else:
            turns -= 1
            print(f"You have {turns} turns remaining")
            if turns == 0:
                print(f"Sorry {player_name}, you ran out of turns. Game over")
                GameBoard.print_board(user_guess_board)
                break

if __name__ == '__main__':
    RunGame()





    