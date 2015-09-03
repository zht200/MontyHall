# Name: Zhitan Zhang
# MontyHall.py
# Plays the Monty Hall Problem game
# Monty Hall Problem has 3 doors, 2 of which have goats and 1 has a car behind them.
# 1 door is picked and 1 door from the left 2 doors that has a goat behind it is opened.
# Then the user can stay with the door picked before or to switch to another door to open.
# If there's a car behind it, the user wins.
# If there's a goat behind it, the user loses.
# The program accepts two command-line arguments: how many games to play and "stay" or "switch"
# Example:
# python3 MontyHall.py 100 stay

import sys
if sys.argv==[''] or len(sys.argv) != 3:
  # default setting
  NGAMES = 10
  POLICY = "switch"
else:
  NGAMES = int(sys.argv[1])
  POLICY = sys.argv[2]

GAMES_NUM = NGAMES
import random
game_won = 0
game_lost = 0
doors = ["g","g","c"]
def runGame():
  global NGAMES, POLICY, game_won, game_lost
  while (NGAMES != 0):
    NGAMES -= 1
    random.shuffle(doors)
    doors_num = [0, 1, 2]
    printList(doors)
    print(", ", end="")
    chosen_num = random.randint(0,2)
    doors_num.remove(chosen_num)
    printList(doors, chosen_num)
    print(", ", end="")
    open_num = -1
    for i in doors_num:
      if doors[i] == "g":
        open_num = i
        break
    printList(doors, chosen_num, open_num)
    print(", ", end="")
    if POLICY == "switch":
      doors_num.remove(open_num)
      chosen_num = doors_num[0]
    printList(doors, chosen_num, open_num, True)
    print()
    if doors[chosen_num] == "c":
      game_won += 1
    else:
      game_lost += 1
  print("Number of games played: " + str(GAMES_NUM))
  print("Player policy: " + str(POLICY))
  print("Number of games won (cars revealed): " + str(game_won))
  print("Number of games lost: " + str(game_lost))
  print("Percentage of games won: " + str(game_won / GAMES_NUM * 100) + "%")
  print("Percentage of games lost: " + str(game_lost / GAMES_NUM * 100) + "%")

def printList(doors, chosen_num = -1, open_num = -1, cap = False):
  print ("[", end="")
  for i in range(3):
    if i == chosen_num:
      print(">", end="")
    if i == open_num or (i == chosen_num and cap == True):
      print(doors[i].upper(), end="")
    else: 
      print(doors[i], end="")
    if i == 2:
      print ("]", end="")
    else:
      print (", ", end="")

if __name__=='__main__':
  runGame()
