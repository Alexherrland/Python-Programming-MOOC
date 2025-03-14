# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        return 1 if len(player1_word) > len(player2_word) else 2 if len(player1_word) < len(player2_word) else 0

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        player1 = sum(1 for letra in player1_word.lower() if letra in "aeiou")
        player2 = sum(1 for letra in player2_word.lower() if letra in "aeiou")
        return 1 if player1 > player2 else 2 if player1 < player2 else 0


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_choice: str, player2_choice: str):
        choices = {"rock", "paper", "scissors"}
        if player1_choice not in choices and player2_choice not in choices:
            return 0
        elif player1_choice not in choices:
            return 2 
        elif player2_choice not in choices:
            return 1 

        rules = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

        if player1_choice == player2_choice:
            return 0 
        elif rules[player1_choice] == player2_choice:
            return 1 
        else:
            return 2 
