# Description: A Tic Tac Toe Game with the Random module for the CPU to make random moves.
# Difficulty: Easy - You can either lose, win or make a tie (CPU almost always loses)

import random as rd # Importing the Random module

# Game Board
board = [" 1 ", " 2 ", " 3 ",
         " 4 ", " 5 ", " 6 ",
         " 7 ", " 8 ", " 9 "]

# Printing the Game Board
def print_board():
  print(f' {board[0]} | {board[1]} | {board[2]}')
  print("-----------------")
  print(f' {board[3]} | {board[4]} | {board[5]}')
  print("-----------------")
  print(f' {board[6]} | {board[7]} | {board[8]}')
  print(" ")


# Player's Turn
def players_turn():
  i = int(input(name + ", enter your move (1-9): "))

  if i > 9:
    print("The number is out of range. Try again!")
    players_turn()

  elif board[i - 1] != "⭕️ " and board[i - 1] != "❌ ":
    board[i - 1] = "❌ "
    print(" ")
    print_board()

  else:
    print("This position is already taken.")
    players_turn()


# CPU's Turn
def cpus_turn():

  i = rd.randint(1,9) # CPU randomly chooses a number between 1 and 9

  if board[i - 1] != "❌ " and board[i - 1] != "⭕️ ":
    board[i - 1] = "⭕️ "
    print(" ")
    print("CPU's move: ")
    print_board()

  else:
    cpus_turn() # Repeat if the position is already taken


# Checking if someone won or if it's a tie
def checkWin():

  if board[0] == "❌ " and board[1] == "❌ " and board[2] == "❌ " or board[3] == "❌ " and board[4] == "❌ " and board[5] == "❌ " or board[6] == "❌ " and board[7] == "❌ " and board[8] == "❌ " or board[0] == "❌ " and board[3] == "❌ " and board[6] == "❌ " or board[1] == "❌ " and board[4] == "❌ " and board[7] == "❌ " or board[2] == "❌ " and board[5] == "❌ " and board[8] == "❌ " or board[0] == "❌ " and board[4] == "❌ " and board[8] == "❌ " or board[2] == "❌ " and board[4] == "❌ " and board[6] == "❌ ":
    print(name + " won!")
    game_active[0] = 1

  elif board[0] == "⭕️ " and board[1] == "⭕️ " and board[2] == "⭕️ " or board[3] == "⭕️ " and board[4] == "⭕️ " and board[5] == "⭕️ " or board[6] == "⭕️ " and board[7] == "⭕️ " and board[8] == "⭕️ " or board[0] == "⭕️ " and board[3] == "⭕️ " and board[6] == "⭕️ " or board[1] == "⭕️ " and board[4] == "⭕️ " and board[7] == "⭕️ " or board[2] == "⭕️ " and board[5] == "⭕️ " and board[8] == "⭕️ " or board[0] == "⭕️ " and board[4] == "⭕️ " and board[8] == "⭕️ " or board[2] == "⭕️ " and board[4] == "⭕️ " and board[6] == "⭕️ ":
    print("CPU won!")
    game_active[0] = 1

  else: 
    for i in range(9):
      if board[i] != "❌ " and board[i] != "⭕️ ":
        break
    else:
      print("It's a tie!")
      game_active[0] = 1


# Game Loop
game_active = [0] # Array to avoid scope variables. 0 stands for yes and 1 stands for no 


# Starting the Game:

print("Welcome to Tic Tac Toe!")
print(" ")
name = input("Enter your name: ")
print(" ")
print_board()

while game_active[0] == 0:
    players_turn()
    checkWin()
    if game_active[0] == 1:
      break
    else:
      cpus_turn()
      checkWin()
