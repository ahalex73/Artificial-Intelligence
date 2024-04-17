# Alexander Holmes
# 4/5/2024
# AI research - How Ai's play chess

# More infomation can be found in the README.txt file, about research, concepts, etc...

# Creating Chess AI Bot using chess python library
# Puts two Chess AI bots against eachother in a Epic Showdown Match or ESM.

# The ESM environment will consist of the terminal, our battlegrounds.


import chess # - https://python-chess.readthedocs.io/en/latest/core.html 
import os    # for clearing terminal
import time

def wait_for_move():
    time.sleep(1.5)
    clear_terminal()

def print_board_and_legal_moves(board):
    print(board.legal_moves)
    print(board)



def learning_chess_library_function():
    board=chess.Board()                         # create board object

    print(board.legal_moves)


    # wait_for_move()
    # print_board_and_legal_moves(board)
    
    # wait_for_move()
    # board.push_san("e4")                        # moving players based on Algebraic Expression or (SAN)
    # print_board_and_legal_moves(board)

    # wait_for_move()
    # board.push_san("Nh6")                        # moving players based on Algebraic Expression or (SAN)
    # print_board_and_legal_moves(board)

    # wait_for_move()
    # board.pop()
    # print_board_and_legal_moves(board)

    # It means moving the particular piece at 
    # e place to 4th position 

    #print(board)                                # Displaying moved chess piece on board 

    # Checking for loss, win, draw.
    # print(board.is_checkmate())                 # Verifying Check Mate - occurs when a king is placed in check and has no legal moves to escape.
    # print(board.is_check())                     # Verifying Check      - a player may not make any move that places or leaves their king in check.
    # print(board.is_stalemate())                 # Verifying Stalemate  - Draw / both players recieve points
    # print(board.is_fivefold_repetition())       # Verifying Fivefold Repetition - If the same position occurs five times during the course of the game, the game is automatically a draw
    # print(board.is_seventyfive_moves())         # Verifying if moves < 75


def clear_terminal():
    """ Clears te terminal screen """
    # Clear terminal based on OS
    if os.name == 'posix': # For Unix/Linux/Mac OS
        os.system('clear')
    elif os.name == 'nt':  # For windows
        os.system('cls')
    else:
        # For other operating systems, print 100 blank lines
        print('\n' * 100)
    

def minimax(depth, board, is_max_player):
    """ Minimax Artificial intelligence algorithm without dataset training """


    

# var minimax = function (depth, game, isMaximisingPlayer) {
#     positionCount++;
#     if (depth === 0) {
#         return -evaluateBoard(game.board());
#     }

#     var newGameMoves = game.ugly_moves();

#     if (isMaximisingPlayer) {
#         var bestMove = -9999;
#         for (var i = 0; i < newGameMoves.length; i++) {
#             game.ugly_move(newGameMoves[i]);
#             bestMove = Math.max(bestMove, minimax(depth - 1, game, !isMaximisingPlayer));
#             game.undo();
#         }
#         return bestMove;
#     } else {
#         var bestMove = 9999;
#         for (var i = 0; i < newGameMoves.length; i++) {
#             game.ugly_move(newGameMoves[i]);
#             bestMove = Math.min(bestMove, minimax(depth - 1, game, !isMaximisingPlayer));
#             game.undo();
#         }
#         return bestMove;
#     }
# };


    return 1

def place_among_us_character():
    board = chess.Board()
    print(board)


def check_board(board):
    """ Checks the board for any game-enders - hopefully returns who wins """
    board_state = board



    return 1
    # return game_ended, 


def move(board):
    # Get board state


    check_board(board)


def main():
    game_ended = False
    # while game_ended == False:
    #     do stuff

    learning_chess_library_function()

    return 1


if __name__ == "__main__":
    main()
