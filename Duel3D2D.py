'''
 * This is a game simulation program that
 * calculates the probability of each player/soldier to stay alive in the battle.
 * Each player/soldier has his strategy.
'''
import random

def duel3d(num):
    '''
    This is a game simulation program for 3 players/soldiers
    :param num: number of simulations
    :return: print the probability of each player/soldier to stay alive in the battle
    '''
    # probability of hitting the target:
    pC, pD, pB = 0.8, 0.5, 1
    # an amount of wins:
    countB, countC, countD = 0, 0, 0
    # id players:
    B, C, D  = 1, 2, 3
    cChance, dChance = 0.00, 0.00
    flag = True
    for i in range(1,num+1):
        # get a list of the shooter order for 3 players:
        q = getQueuq3()
        first = q[0]
        if first == 1: # B is the first and B kills C
            dChance = random.random() # D fire
            if dChance < pD:
                countD += 1  # D kills B
            else:
                countB += 1  # B kills D
            continue
        elif first == 2: # C is the first, C try to kill B
            cChance = random.random()  # C fire
            if cChance < pC:  # C kills B, duel between C and D
                flag = True
                while flag:
                    dChance = random.random() # D fire
                    if dChance < pD: # C is killed
                        countD += 1
                        flag = False
                    else:
                        cChance = random.random()  # C fire
                        if cChance < pC:  # D is killed
                            countC += 1
                            flag = False
            # C does not kill B,  the triple duel B, C, D:
            elif q[1] == B: # B is the second, B kills C
                dChance = random.random()  # D fire, try to kill B
                if dChance < pD:
                    countD += 1  # D kills B
                else:
                    countB += 1  # B kills D
            elif q[1] == D: # D is the second, D does not fire
                # B kills C
                dChance = random.random()  # D fire, try to kill B
                if dChance < pD:
                    countD += 1  # D kills B
                else:
                    countB += 1  # B kills D
            continue
        elif first == 3: # D is the first, D does not fire
            if q[1] == B:  # B is the second, B kills C
                dChance = random.random()  # D fire, try to kill B
                if dChance < pD:
                    countD += 1  # D kills B
                else:
                    countB += 1  # B kills D
            else:
                if q[1] == C:  #  C is the second, C try to kill B
                    cChance = random.random()  # C fire
                    if cChance < pC:  # C kills B, duel between C and D
                        flag = True
                        while flag:
                            dChance = random.random()  # D fire
                            if dChance < pD:  # C is killed
                                countD += 1
                                flag = False
                            else:
                                cChance = random.random()  # C fire
                                if cChance < pC:  # D is killed
                                    countC += 1
                                    flag = False
                    else:
                        # C does not kill B, B kills C
                        dChance = random.random()  # D fire, try to kill B
                        if dChance < pD:
                            countD += 1  # D kills B
                        else:
                            countB += 1  # B kills D
            continue
    print("Three battle: countB =", countB, ", countC =", countC, ", countD =", countD)
    probB = float(countB/num)
    probC = float(countC/num)
    probD = float(countD/num)
    print("probB =", probB, ", probC =", probC, ", probD =", probD)
    print("summa =", float(probB+probC+probD))

def getQueuq3():
    '''
    Get a random list of the shooter order for 3 players:
    :return: a random list of the shooter order for 3 players:
    '''
    q = [[1, 2, 3], [1, 3, 2], [3, 1, 2], [3, 2, 1], [2, 1, 3], [2, 3, 1]]
    rand = random.randint(0, 5)
    return q[rand]

def duel2d(num):
    '''
    This is a game simulation program for 2 players/soldiers
    :param num: number of simulations
    :return: print the probability of each player/soldier to stay alive in the battle
    '''
    # probability of hitting the target:
    pC, pB = 0.8, 1
    # an amount of wins:
    countB, countC = 0, 0
    # id players:  B, C  = 1, 2
    cChance = 0.00
    for i in range(1, num + 1):
        first = random.randint(1,2)
        if first == 1:  # B is the first and B kills C
            countB += 1  # B kills C
            continue
        elif first == 2: # C is the first, C try to kill B
            cChance = random.random()  # C fire, try to kill B
            if cChance < pC:
                countC += 1  # C kills B
            else:
                countB += 1  # C does not kill B, B kills C
            continue

    print("Duel: countB =", countB, ", countC =", countC)
    probB = float(countB/num)
    probC = float(countC/num)

    print("probB =", probB, ", probC =", probC)
    print("summa =", float(probB+probC))

###############################################################
num = 5000000
duel2d(num)
duel3d(num)