import random
from collections import defaultdict



class GameLogic:

    @staticmethod
    def roll_dice(rolled_dice):
        dice_list = []
        for _ in range(rolled_dice):
            dice_list.append(random.randint(1,6))
        return tuple(dice_list)

    @staticmethod
    def calculate_score(tup):
        score = 0
        # Sorted tupple into a list for straight
        sorttup = sorted(tup)
        freq = defaultdict(int)
        # Empty list for three pairs
        threepairs = []
        #Number frequency
        
        for el in tup:
                freq[el] += 1
        # print(freq.items())

        #Three pairs
        for key , y in freq.items():
            if y == 2:
                threepairs.append(key)
            if len(threepairs) == 3:
                score = 1500

        # Straight
        if sorttup == [1,2,3,4,5,6]:
            score = 1500
        else: 
            for key, y in freq.items():
                # 3 or more 1s
                if key == 1 and y > 2:
                    if y == 3:
                        score += 1000
                    elif y == 4:
                        score += 2000
                    elif y == 5:
                        score += 3000
                    elif y == 6:
                        score += 4000
                elif y == 6:
                    score += (key * 100)*4
                elif y == 5:
                    score += (key * 100)*3
                elif y == 4:
                    score += (key * 100)*2
                elif y == 3:
                    score += (key * 100)
                # 1 occurance of the values 1 and 5
                elif y == 1 :
                    if key == 5:
                        score += 50
                    elif key == 1:
                        score += 100
                # 2 occurances of the values 1 and 5
                elif y == 2:
                    if key == 5:
                        score += 100
                    elif key == 1:
                        score += 200
        return score



# if __name__=='__main__':
    # GameLogic.calculate_score(tup) 