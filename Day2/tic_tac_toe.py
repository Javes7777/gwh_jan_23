## python game tic tac toe, text based
## can be played on console.
import os
import sys
import random

game_board_row="-----------------"

winning_moves=[[1,2,3,], [4,5,6], [7,8,9],
                [1,5,9], [7,5,3],
                [1,4,7], [3,6,9], [2,5,8]]
tic="  X  "
tac="  O  "

playing = True

inst="""
    Enter a number to make a put your move on grid
    The numbers in grid are mapped as:
    1  |  2  |  3
    -------------
    4  |  5  |  6
    -------------
    7  |  8  |  9
"""

menu="""
    Welcome to tic tac toe.
    1. Play
    2. Instructions
    3. HighScores
    4. Exit
"""

def print_score(winner):
    print(winner)
    if winner == None:
        print("Its a draw")
    elif winner == True:
        print("Congratulations you won!")
    else: 
        print("Try again next time.")


def print_board(player_moves, cpu_moves):
    os.system("clear")
    for i in range(1, 10):
        if i in player_moves:
            print(tic, end='')
        elif i in cpu_moves:
            print(tac, end='')
        else: 
            #print('  {0}  '.format(i), end='')
            print('     ', end='')
        
        if i not in [3,6,9]:
            print('|', end='')
        elif i != 9:
            print('')
            print(game_board_row)

    print()


def play_against(player_moves):
    while True:
        move = random.randint(1,9)
        if move not in player_moves:
            return move  

def check_winner(player_moves):
    for seq in range(0, len(winning_moves)):
        if set(winning_moves[seq]) <= set(player_moves):
            return True
    return False

def play():
    player_moves=[]
    cpu_moves=[]
    print_board(player_moves, cpu_moves)
    while True:
        num = int(input("Enter your move: "))
        if num in range(1,10) and num not in cpu_moves:
            player_moves.append(num)
            print_board(player_moves, cpu_moves)
            if check_winner(player_moves) == True:
                return True
            if len(player_moves) + len(cpu_moves) == 9: 
                return None
           
            cpu_moves.append(play_against(player_moves))
            print_board(player_moves, cpu_moves)
            if check_winner(cpu_moves) == True:
                return False
            if len(player_moves) + len(cpu_moves) == 9: 
                return None
        else:
            print("please Enter a valid num(1-9)")

    
if __name__ == '__main__':
    win_count=0
    loss_count=0
    num_games=0
    while True:
        print(menu)
        prompt = input("Enter choice: ")
        if prompt == "1":
            num_games+=1
            os.system('clear')
            winner = play()
            if winner==True:
                win_count+=1
            elif winner==False:
                loss_count+=1
            print_score(winner)
        elif prompt == "2":
            print(inst)
        elif prompt == "3":
            print("Played {0} times".format(num_games))
            print("Won {0} times".format(win_count))
            print("Lost {0} times".format(loss_count))
            print("Draw {0} times".format(num_games-(loss_count+win_count)))
        else: 
            os.system('clear')
            print("\nThanks for playing today!!")
            break





