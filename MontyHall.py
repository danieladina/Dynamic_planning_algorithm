import random
'''
/**
 * This class presents random simulations of the Monty Hall game,
 * using three doors for each strategy and shows the results in such a way 
 * as to make it easy to compare the effects of each strategy.
 * It shows the effects of a strategy of the contestant always keeping his first guess 
 * so it can be contrasted with the strategy of the contestant always switching his guess.
 * A YouTube video: https://www.youtube.com/watch?v=4Lb-6rxZxx0
 */
'''

def mothy_hall_game():
    switchWins, stayWins = 0, 0
    ROUNDS = 1000000 #32768
    for plays in range(0, ROUNDS):
        doors = [0, 0, 0]; # 0 is a goat, 1 is a car

        doors[random.randint(0,2)] = 1 # put a winner in a random door
        choice = random.randint(0,2) # pick a door, any door
        shown = random.randint(0, 2) # the shown door

        while doors[shown] == 1 or shown == choice:
            shown = random.randint(0, 2) # //don't show the winner or the choice

        stayWins += int(doors[choice]) # if you won by staying, count it
        # the switched (last remaining) door is (3 - choice - shown), because 0+1+2=3
        switchWins += doors[3 - int(choice) - int(shown)]

    print("Switching wins", switchWins,"times. The probability of winning is",float(switchWins/1000000))
    print("Staying wins", stayWins,"times. The probability of winning is",float(stayWins/1000000))

mothy_hall_game()

'''
Switching wins 666748 times.
Staying wins 333252 times.
'''