def is_valid_chess(board):
    bk = 0
    wk = 0
    wp = 0
    bp = 0
    black_pieces = 0
    white_pieces = 0

    for key in board:
        if key[0] not in 'hgfedcba':
            print("This is not a valid chessboard!")
            return False
        if key[1] not in '87654321':
            print("This is not a valid chessboard!")
            return False

  
    for value in board.values():
        if value[0] not in ('w', 'b'):
            print("This is not a valid chessboard!")
            return False
        if value[1] not in ('P', 'N', 'B', 'R', 'Q', 'K'):
            print("This is not a valid chessboard!")
            return False
        if value[0] == 'w':
            white_pieces+=1
        if value[0] == 'b':
            black_pieces+=1

        if value == 'bP':
            bp+=1
        elif value == 'wP':
            wp+=1
        if bp > 8 or wp > 8:
            print("This is not a valid chessboard!")
            return False
        if value == 'bK':
            bk+=1
        elif value == 'wK':
            wk+=1
        if bk > 1 or wk > 1:
            print("This is not a valid chessboard!")
            return False

    if white_pieces > 16 or black_pieces > 16:
        print("This is not a valid chessboard!")
        return False
    
    return True


valid_board = {'a1': 'wP', 'a2': 'wP', 'a3': 'wP', 'a4': 'wP', 'a5': 'wP', 'a6': 'wP', 'a7': 'wP', 'a8': 'wP'}

is_valid_chess(valid_board)