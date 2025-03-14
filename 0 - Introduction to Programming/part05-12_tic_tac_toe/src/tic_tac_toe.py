# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str):
    if x > 2 or y > 2 or x < 0 or y < 0:
        return False
    for i, row in enumerate(game_board):
        for j, value in enumerate(row):
            if j + i*3 == x*3 + y:
                if game_board[j][i] == "":
                    game_board[j][i] = piece
                    return True
                else:
                    return False

if __name__ == "__main__":
    game_board = [['', '', 'O'], ['', 'X', 'O'], ['', '', '']]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)