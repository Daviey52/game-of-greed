# Game of Greed

- Authors: Chris Rarig and David Waiganjo

- Game: a command line version of the dice game Game of Greed

## Lab 01

1. Define a `GameLogic` class in game_of_greed/game_logic.py file.
2. Handle calculating score for dice roll
3. Handle rolling dice
4. Handle banking points

## Lab 02

1. Application should simulate rolling between 1 and 6 dice
2. Application should allow user to set aside dice each roll
3. Application should allow “banking” current score or rolling again.
4. Application should keep track of total score
5. Application should keep track of current round
6. Application should have automated tests to ensure proper operation

## Lab 03

1. Application should implement features from versions 1 and 2
2. Should handle setting aside scoring dice and continuing turn with remaining dice.
3. Should handle when cheating occurs.
      Or just typos.
    E.g. roll = [1,3,5,2] and user selects 1, 1, 1, 1, 1, 1
4. Should allow user to continue rolling with 6 new dice when all dice have scored      in current turn.
5. Handle zilch
    No points for round, and round is over

## Lab 04

1. Create an AI Bot to play Game of Greed
    The only method available for use from Game class is play.
    All static methods of GameLogic class are available.
   All other interactions with game can take place ONLY via the I/O features of the game.
      In other words, via injectable print and input functionality.
      It is FORBIDDEN to inject a custom roller function into Game class.
2. Copy bots.py to your project.
   Place it at root of project, at same level as pyproject.toml
3. Your Bot class should be added to bots.py file with name of your choosing replacing YourBot.
   NOTE the code for BaseBot class is supplied for reference, but your custom code will be in the overridden _roll_bank_or_quit and _enter_dice methods.
4. User should be able to see your bot play by executing bots.py from terminal.
5. Application should implement features from previous classes

## Github

- [Repo](https://github.com/Daviey52/game-of-greed)
- [Lab 01 Pull Request](https://github.com/Daviey52/game-of-greed/pull/2)

- [Lab 02 Pull Request](https://github.com/Daviey52/game-of-greed/pull/6)

- [Lab 03 Pull Request](https://github.com/Daviey52/game-of-greed/pull/16)

- [Lab 04 Pull Request](https://github.com/Daviey52/game-of-greed/pull/18)

## Resources Used

- [python-elements-frequency-in-tuple](https://www.geeksforgeeks.org/python-elements-frequency-in-tuple/)

- [Python Set issubset() Method](https://www.w3schools.com/python/ref_set_issubset.asp#:~:text=Python%20Set%20issubset%20%28%29%20Method%201%20Definition%20and,all%20items%20are%20present%20in%20the%20specified%20set%3F)

- [issubset()-in-python](https://www.tutorialspoint.com/issubset-in-python)

## Credit

- Roger Huba
