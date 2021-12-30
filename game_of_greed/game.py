from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    def __init__(self):
        self.count = 0
        self.score = 0

    def play(self, roller=None):

        roller = roller or GameLogic.roll_dice
        dice = 6
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        play_option = input("> ")
        start_game = True

        if play_option.lower() == "n":
            print("OK. Maybe another time")
            start_game = False

        while start_game:

            if play_option.lower() == "y":
                self.count += 1

                print(f"Starting round {self.count}")
                print(f"Rolling {dice} dice ...")
                dice -= 1
                playing = roller(dice)
                roll_No = " "
