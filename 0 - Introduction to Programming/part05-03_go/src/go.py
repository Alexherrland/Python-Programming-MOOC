# Write your solution here
def who_won(game_board: list):
    player1 = 0
    player2 = 0
    for col in game_board:
        for row in col:
            if row == 1:
                player1 +=1
            elif row == 2:
                player2 +=1
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0

    