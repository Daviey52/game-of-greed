# from game_logic import GameLogic
# from banker import Banker

from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    def __init__(self, count = 0, score = 0):
        self.count = count
        self.score = score



    def play(self, roller=None):
        roller = roller or GameLogic.roll_dice
        
        rounds = 0
        dice = 6
        score = 0
        banked = 0
        
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        play_option = input("> ")
        start_game = True

        if play_option.lower() == "n":
            print("OK. Maybe another time")
            start_game = False

        while start_game:
            
            if play_option.lower() == "y":
                rounds += 1
                print(f"Starting round {rounds}")
                print(f"Rolling {dice} dice...")
                playing = roller(dice)
                roll_No = ""
                for roll in playing:
                    roll_No = roll_No + str(roll)+ " "
                print(f"*** {roll_No}***")
                print("Enter dice to keep, or (q)uit:")
                play_option = input("> ")
            elif play_option.lower() == "q":
                print(f"Thanks for playing. You earned {banked} points")
                start_game = False
            elif play_option.lower() == "b":
                banked += (Banker.bank(Banker))
                print(f"You banked {score} points in round {rounds}")
                print(f"Total score is {banked} points")
                rounds += 1
                dice = 6
                print(f"Starting round {rounds}")
                print(f"Rolling {dice} dice...")
                playing = roller(dice)
                roll_No = ""
                for roll in playing:
                    roll_No = roll_No + str(roll)+ " "
                print(f"*** {roll_No}***")
                print("Enter dice to keep, or (q)uit:")
                play_option = input("> ")
            elif play_option.lower() == "r":
                print(f"Rolling {dice} dice...")
                playing = roller(dice)
                roll_No = ""
                for roll in playing:
                    roll_No = roll_No + str(roll)+ " "
                print(f"*** {roll_No}***")
                print("Enter dice to keep, or (q)uit:")
                play_option = input("> ")
            elif int(play_option):
                score = 0
                val = [int(i) for i in play_option]
                score += GameLogic.calculate_score(val)
                shelved = (Banker.shelf(Banker,score))
                dice -= len(val)
                print(f"You have {shelved} unbanked points and {dice} dice remaining")
                print('(r)oll again, (b)ank your points or (q)uit:')
                play_option = input("> ")

                

    # def includes(self,value,ll):
    #     current = ll.head
    #     while current != None:
    #         if current.value == value:
    #             return True
    #         current = current.next
    #     return False 

if __name__=='__main__':
    Game.play(1) 