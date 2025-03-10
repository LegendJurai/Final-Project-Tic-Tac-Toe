# Description: A Tic Tac Toe Game with the MiniMax Algorithm for the CPU to make the best move
# Difficulty: Hard - You can either lose or make a tie (CPU never loses)

# Implementing the Game Board with rows and columns for using the Minimax Algorithm
board_1 = [
        [" 1 ", " 2 ", " 3 "], # Index 0 --> inner index 0, 1, 2
        [" 4 ", " 5 ", " 6 "], # Index 1 --> inner index 0, 1, 2
        [" 7 ", " 8 ", " 9 "]  # Index 2 --> inner index 0, 1, 2
] 
# Game Board for Player's input
board_2 =[
        " 1 ", " 2 ", " 3 ", 
        " 4 ", " 5 ", " 6 ", 
        " 7 ", " 8 ", " 9 "  
] 

# Creating player (you) and cpu (class)
class Player:
    def __init__(self, name, symbol, isMaxPlayer):
        self.name = name
        self.symbol = symbol #  X or O
        self.isMaxPlayer = isMaxPlayer # Player is Max, CPU is Min

# Player's Turn:
    def players_turn(self):
      i = int(input(self.name + ", enter your move (1-9): "))

      if i < 1 or i > 9:
        print("The number is out of range. Try again!")
        self.players_turn()

      elif board_2[i - 1] != player_instance.symbol and board_2[i - 1] != cpu.symbol:
        board_2[i - 1] = player_instance.symbol
        board_index() # Update the board_1 with the new move
        print(" ")
        print_board()

      else:
        print("This position is already taken.")
        player_instance.players_turn()

# Computer's Turn:
    def cpus_turn(self):
      bestVal = 1000 # +infinity
      bestMove = (1, 1) # (row, column)
      # Going through the whole Game Board to find the best move
      for row in range(3):
        for column in range(3):

          if board_1[row][column] != player_instance.symbol and board_1[row][column] != cpu.symbol:
            backup = board_1[row][column] # Backup the current value
            board_1[row][column] = cpu.symbol
            moveVal = minimax(board_1, 0, True) # Using the MiniMax Algorithm for every empty space
            board_1[row][column] = backup # Undo the move

            if moveVal < bestVal:
              bestMove = (row, column)
              bestVal = moveVal

      board_1[bestMove[0]][bestMove[1]] = cpu.symbol # CPU doing the move

      board_index_2() # Update the board_2 with the new move
      print(" ")
      print("CPU's move: ")
      print_board()
        

# Creating player and cpu instances after class definition
print("Welcome to Tic Tac Toe!")
print(" ")
name_of_player = input("Enter your name: ")
print(" ")
player_instance = Player(name_of_player, "❌ ", True)
cpu = Player("CPU", "⭕️ ", False)


# Check if there are any moves left  
def isMovesLeft(board_1) :  
    # Going through the whole Game Board to find empty spaces
    for row in range(3) : 
        for column in range(3) : 
            
            if board_1[row][column] != player_instance.symbol and board_1[row][column] != cpu.symbol: 
                return True 
    return False


# Evaluation function (CPU knows how to win the Game in the MiniMax Algorithm)
def evaluate(b, depth):
  # Looking for a winner in rows (horizontal)
  for row in range(3):

    if b[row][0] == b[row][1] and b[row][1] == b[row][2]:

      if b[row][0] == player_instance.symbol:
        return 10 - depth
      
      elif b[row][0] == cpu.symbol:
        return -10 + depth

  # Looking for a winner in columns (vertical)
  for column in range(3):

    if b[0][column] == b[1][column] and b[1][column] == b[2][column]:

      if b[0][column] == player_instance.symbol:
        return 10 - depth
      
      elif b[0][column] == cpu.symbol:
        return -10 + depth

  # Looking for a winner in diagonals
  if b[0][0] == b[1][1] and b[1][1] == b[2][2] or b[0][2] == b[1][1] and b[1][1] == b[2][0]:

    if b[1][1] == player_instance.symbol:
      return 10 - depth
    
    elif b[1][1] == cpu.symbol:
      return -10 + depth
  
  else:
    return 0


# Minimax algorithm (for the CPU to make the best move)
def minimax(board_1, depth, isMaxPlayer):
  for _ in range(9 - depth): # To avoid the "RecursionError: maximum recursion depth exceeded in comparison"

    score = evaluate(board_1, depth)

    if score == 10 - depth:
      return score  
    elif score == -10 + depth:
      return score 

    if isMovesLeft(board_1) == False:
      return 0

    # Maximizer's turn
    if isMaxPlayer == True:
      best = -1000 # -infinity
      # Going through the whole Game Board to find the best move
      for row in range(3):
        for column in range(3):

          if board_1[row][column] != player_instance.symbol and board_1[row][column] != cpu.symbol:
            backup = board_1[row][column] # Backup the current value
            board_1[row][column] = player_instance.symbol # Player's move (X)
            best = max(best, minimax(board_1, depth + 1, False)) # MiniMax-Recursion to CPU (Minimizer)
            # print(best) --> to test
            board_1[row][column] = backup # Undo the move
      return best
    
    # Minimizer's turn      
    else:
      best = 1000 # +infinity
      # Going through the whole Game Board to find the best move
      for row in range(3):
        for column in range(3):

          if board_1[row][column] != cpu.symbol and board_1[row][column] != player_instance.symbol:
            backup = board_1[row][column] # Backup the current value
            board_1[row][column] = cpu.symbol # CPU's move (O)
            best = min(best, minimax(board_1, depth + 1, True)) # MiniMax-Recursion to Player (Maximizer)
            # print(best) --> to test
            board_1[row][column] = backup # Undo the move
    return best


# Printing the Game Board
def print_board():
  print(f' {board_1[0][0]} | {board_1[0][1]} | {board_1[0][2]}')
  print("-----------------")
  print(f' {board_1[1][0]} | {board_1[1][1]} | {board_1[1][2]}')
  print("-----------------")
  print(f' {board_1[2][0]} | {board_1[2][1]} | {board_1[2][2]}')
  print(" ")

# Updating board_1 with the player's move
def board_index():
  board_1[0][0] = board_2[0]
  board_1[0][1] = board_2[1]
  board_1[0][2] = board_2[2]
  board_1[1][0] = board_2[3]
  board_1[1][1] = board_2[4]
  board_1[1][2] = board_2[5]
  board_1[2][0] = board_2[6]
  board_1[2][1] = board_2[7]
  board_1[2][2] = board_2[8]

# Updating board_2 with the CPU's move
def board_index_2():
  board_2[0] = board_1[0][0]
  board_2[1] = board_1[0][1]
  board_2[2] = board_1[0][2]
  board_2[3] = board_1[1][0]
  board_2[4] = board_1[1][1]
  board_2[5] = board_1[1][2]
  board_2[6] = board_1[2][0]
  board_2[7] = board_1[2][1]
  board_2[8] = board_1[2][2]
  
# Check if there is a winner or a tie
def checkWin():
  score = evaluate(board_1, 0)
  if score == 10:
    print(name_of_player + " won!")
    game_active[0] = 1
  elif score == -10:
    print("CPU won!")
    game_active[0] = 1
  elif isMovesLeft(board_1) == False:
    print("It's a tie!")
    game_active[0] = 1
  
# Game Loop
game_active = [0] # Array to avoid scope variables. 0 stands for yes and 1 stands for no 


# Starting the Game:

print_board()

while game_active[0] == 0:
    player_instance.players_turn()
    checkWin()
    if game_active[0] == 1:
      break
    else:
      cpu.cpus_turn()
      checkWin()
