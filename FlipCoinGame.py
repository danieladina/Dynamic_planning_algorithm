'''
 * Alice and Bob  - flip coin game:
 * Strategy 1. Alice calls a random number - Probability ½
 * Strategy 2. Alice calls 1 and Bob calls 1 - Probability ¾
 * Strategy 2A. Alice calls 0 and Bob calls 0 - Probability ¾
 * Strategy 3. Everyone says that he (she) received - Probability ½
 * Strategy 4. Alice calls that she got and
 * 			   Bob calls the opposite of what he received -
 * 			   Probability 1
'''

from random import randint
from operator import xor    # Optional. There are alternatives


def flip_coin():
    '''
    method returns 0 or 1 randomly
    :return: returns 0 or 1 randomly
    '''
    return randint(0, 1)


def alice_game():
    '''
    method returns result of Alice
    :return: returns 0 or 1 randomly
    '''
    return flip_coin()


def bob_game():
    '''
    method returns result of Bob
    :return: returns 0 or 1 randomly
    '''
    return flip_coin()


# Alice calls a random number - Probability 0.5
def game_strategy1():
    result = True if alice_game() > 0 else False
    return result


# Alice calls 1 and Bob calls 1 - Probability 0.75
# symmetric: Alice calls 0 and Bob calls 0
def game_strategy2():
    result = True if alice_game() == 1 or bob_game() == 1 else False
    return result


# Everyone says that s/he received - Probability 0.5
def game_strategy3():
    result = True if alice_game() == bob_game() else False
    return result


# Alice calls that she got, Bob calls the opposite of what he received - Probability 1
def game_strategy4():
    alice, bob = alice_game(), bob_game()
    result = True if (alice == bob) or xor(bob, alice) else False
    # result = True if (alice == bob) or (bob ^ alice) else False
    # result = True if (alice == bob) or (bob == 1 - alice) else False
    # result = True if (alice == bob) or (bob != alice) else False
    return result


def main():
    count = 1000000
    strategy_lst = [0] * 4  # [0,0,0,0]
    for i in range(count):
        strategy_lst[0] += game_strategy1()
        strategy_lst[1] += game_strategy2()
        strategy_lst[2] += game_strategy3()
        strategy_lst[3] += game_strategy4()
    for i in range(len(strategy_lst)):
        print(f"Strategy{i + 1} probability ==>", strategy_lst[i] / count)


if __name__ == '__main__':
    main()
