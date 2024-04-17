# Alexander Holmes
# 4/5/2024
# AI research - How Ai's play chess

# More infomation can be found in the README.txt file, about research, concepts, etc...

# Creating Chess AI Bot using chess python library
# Puts two Chess AI bots against eachother in a Epic Showdown Match or ESM.

# The ESM environment will consist of the terminal, our battlegrounds.

import chess
import random
import time
import os

# Function to evaluate the board position
def evaluate_board(board):
    # Count material advantage for each side
    white_score = sum([piece_value_white(piece) for piece in board.piece_map().values() if piece.color == chess.WHITE])
    black_score = sum([piece_value_black(piece) for piece in board.piece_map().values() if piece.color == chess.BLACK])

    # Evaluate king safety
    white_king_safety = king_safety(board, chess.WHITE)
    black_king_safety = king_safety(board, chess.BLACK)

     # Evaluate pawn structure
    white_pawn_structure = pawn_structure(board, chess.WHITE)
    black_pawn_structure = pawn_structure(board, chess.BLACK)

    # Evaluate piece activity and mobility
    white_mobility = len(list(board.legal_moves)) / 100
    black_mobility = -len(list(board.legal_moves)) / 100

    # Combine all factors
    evaluation = (white_score - black_score) + (white_king_safety - black_king_safety) + (white_pawn_structure - black_pawn_structure) + (white_mobility + black_mobility)
    
    return evaluation

def king_safety(board, color):
    """ Evaluate score for king safety """
    # Check if king is castled
    king_square = board.king(color)
    if king_square is None:
        return 0
    
    # Evaluate king's position
    king_file, king_rank = chess.square_file(king_square), chess.square_rank(king_square)
    king_safety_score = 0

    # Penalty for not castling
    if king_square != chess.E1 and king_square != chess.E8:
        king_safety_score -= 10
    
    # Check for pawn shield - When the king has castled, it is important to preserve pawns next to it, in order to protect it against an assault. 
    pawn_shield_score = 0
    if color == chess.WHITE:
        target_rank = min(7, king_rank + 1)  # Ensure target rank is within bounds
    else:
        target_rank = max(0, king_rank - 1)  # Ensure target rank is within bounds

    for file in range(max(0, king_file - 1), min(7, king_file + 2)):
        if board.piece_at(chess.square(file, target_rank)) == chess.Piece(chess.PAWN, color):
            pawn_shield_score += 1
    king_safety_score += pawn_shield_score * 5
    
    return king_safety_score

def pawn_structure(board, color):
    """ Evaluate a structure compared to other pawns"""
    pawn_structure_score = 0
    for square in board.pieces(chess.PAWN, color):
        pawn_structure_score += pawn_structure_eval(board, square, color)
    return pawn_structure_score

# Bonus for good pawn structure
def pawn_structure_eval(board, square, color):
    """ Evaluate pawns based on pawn structure (Neighboring pawns) """

    bonus = 0
    pawn = chess.square_file(square), chess.square_rank(square)
    if color == chess.WHITE:
        for i in range(1, 4):
            if board.piece_at(chess.square(pawn[0], pawn[1] + i)) == chess.Piece(chess.PAWN, color):
                bonus += 1
            else:
                break
    else:
        for i in range(1, 4):
            if board.piece_at(chess.square(pawn[0], pawn[1] - i)) == chess.Piece(chess.PAWN, color):
                bonus += 1
            else:
                break
    return bonus

# Assign values to each piece
def piece_value_white(piece):
    if piece.piece_type == chess.PAWN:
        return 1
    elif piece.piece_type == chess.KNIGHT:
        return 3
    elif piece.piece_type == chess.BISHOP:
        return 3
    elif piece.piece_type == chess.ROOK:
        return 5
    elif piece.piece_type == chess.QUEEN:
        return 9
    elif piece.piece_type == chess.KING:
        return 100
    return 0

def piece_value_black(piece):
    if piece.piece_type == chess.PAWN:
        return -1
    elif piece.piece_type == chess.KNIGHT:
        return -3
    elif piece.piece_type == chess.BISHOP:
        return -3
    elif piece.piece_type == chess.ROOK:
        return -5
    elif piece.piece_type == chess.QUEEN:
        return -9
    elif piece.piece_type == chess.KING:
        return -100
    return 0

# Minimax function with alpha-beta pruning to find the best move
def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function for bot with minimax algorithm using alpha-beta pruning
def minimax_bot_alpha_beta(board, depth):
    best_move = None
    max_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    for move in board.legal_moves:
        board.push(move)
        eval = minimax_alpha_beta(board, depth - 1, alpha, beta, False)
        board.pop()
        if eval > max_eval:
            max_eval = eval
            best_move = move
        alpha = max(alpha, eval)
    return best_move

# Function for bot with random placement
def random_bot(board):
    """ Returns a randomly chosen spot to move """
    return random.choice(list(board.legal_moves))

def clear_terminal():
    """ Clears terminal - should hopefully work on all OS"""
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

# def wait_for_move():
#     time.sleep(.2)
#     clear_terminal()

def print_board(board):
    """ Prints out board with better unicode characters than the chess library had """
    clear_terminal()
    pieces_unicode = {'p': '♙', 'n': '♘', 'b': '♗', 'r': '♖', 'q': '♕', 'k': '♔',
                      'P': '♟', 'N': '♞', 'B': '♝', 'R': '♜', 'Q': '♛', 'K': '♚', '.': '·'}
    board_str = ''
    for rank in range(7, -1, -1):
        for file in range(8):
            piece = board.piece_at(chess.square(file, rank))
            if piece is not None:
                board_str += pieces_unicode[piece.symbol()]
            else:
                board_str += pieces_unicode['.']
            board_str += '  '
        board_str += '\n'
    print("Random moves (Black)\n")
    print(board_str)
    print("Minimax with alpha and beta pruning (White)")


def main():
    board = chess.Board()
    depth = 3  # Depth of search for Minimax-alpha-beta-pruning algorithm
    moves_without_capture_or_pawn_move = 0

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            move = minimax_bot_alpha_beta(board, depth)
        else:
            move = random_bot(board)
        print_board(board)

        board.push(move)

        # Check for insufficient material
        if board.is_insufficient_material():
            print("Insufficient material! The game is a draw.")
            break

        # Check for seventy-five move rule
        if board.can_claim_fifty_moves() or moves_without_capture_or_pawn_move >= 150:
            print("Seventy-five move rule! The game is a draw.")
            break

        # Check for fivefold repetition
        if board.is_fivefold_repetition():
            print("Fivefold repetition! The game is a draw.")
            break

        # Check for draw by threefold repetition
        if board.is_seventyfive_moves():
            print("Draw by seventy-five move rule.")
            break

        # Update moves without capture or pawn move
        if move in board.move_stack:
            moves_without_capture_or_pawn_move += 1
        else:
            moves_without_capture_or_pawn_move = 0

    print("Game Over")
    print("Result: " + board.result())

if __name__ == "__main__":
    main()







