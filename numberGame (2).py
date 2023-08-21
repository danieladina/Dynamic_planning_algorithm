'''
 * Game of numbers
 * There are 2*n numbers in a line:
 * a0, a1, a2, a3, ... , a2n-4, a2n-3, a2n-2, a2n-1
 * Two players take the number one by one
 * from one of the ends of the line until there are no more numbers left.
 * The player with the larger sum of numbers wins.
'''

'''
 * Greedy algorithm:
 * A greedy algorithm is an algorithmic paradigm that follows 
 * the problem solving of making the locally optimal choice 
 * at each stage with the hope of finding a global optimum.
'''


def GreedyAlgorithm(arr):
    alice_result = 0
    bob_result = 0
    begin = 0
    end = len(arr) - 1
    step = 1
    print("*********** THIS IS A GAME **********")
    print(arr)
    while end > begin:
        print("******* step #", step, "*******")
        # ***** First player ( Alice ) choice *****
        print(arr[begin:end + 1])
        if arr[begin] > arr[end]:
            print("ALICE: I take the first:", arr[begin])
            alice_result += arr[begin]
            begin += 1
        else:
            print("ALICE: I take the last:", arr[end])
            alice_result += arr[end]
            end -= 1
        # ***** Second player ( Bob ) choice *****
        print(arr[begin:end + 1])
        if arr[begin] > arr[end]:
            print("BOB: I take the first:", arr[begin])
            bob_result += arr[begin]
            begin += 1
        else:
            print("BOB: I take the last:", arr[end])
            bob_result += arr[end]
            end -= 1
        step += 1
        print("Sum - ALICE:", alice_result, ", BOB:", bob_result)
    print("Congratulations! ALICE =", alice_result, ", BOB =", bob_result)


#########################################################################
'''
 * Even Odd Algorithm is not optimal almost:
 * compare between sum of elements at even index 
 * and elements at odd index - once
 * assumption - size is even
 * Complexity: O(n)
 * Calculate the sum of all numbers that are odd-numbered.
 * Calculate the sum of all numbers that are even-numbered.
 * The first player can choose the number standing on an even or odd place (where sum is bigger).
 * If the first player chooses the number standing on an even place,
 * the second player can choose the number standing on an odd place and vice versa.
'''


def OddEvenAlgorithm(arr):
    alice_result = 0
    bob_result = 0
    begin = 0
    end = len(arr) - 1
    odd_sum = 0
    even_sum = 0
    for i in range(0, len(arr), 2):
        even_sum += arr[i]
        odd_sum += arr[i + 1]
    even = True if even_sum > odd_sum else False
    step = 1
    print("*********** THIS IS A GAME **********")
    print(arr)
    while end > begin:
        print("******* step #", step, "*******")
        # ***** First player ( Alice ) choice *****
        print(arr[begin:end + 1])
        if (even and begin % 2 == 0) or (even != True and begin % 2 != 0):
            print("ALICE: I take the first:", arr[begin])
            alice_result += arr[begin]
            begin += 1
        else:
            print("ALICE: I take the last:", arr[end])
            alice_result += arr[end]
            end -= 1
        # ***** Second player ( Bob ) choice *****
        print(arr[begin:end + 1])
        if arr[begin] > arr[end]:
            print("BOB: I take the first:", arr[begin])
            bob_result += arr[begin]
            begin += 1
        else:
            print("BOB: I take the last:", arr[end])
            bob_result += arr[end]
            end -= 1
        step += 1
        print("Sum - ALICE:", alice_result, ", BOB:", bob_result)
    print("Congratulations! ALICE =", alice_result, ", BOB =", bob_result)


#########################################################################

def AdaptiveAlgorithm(arr):
    alice_result = 0
    bob_result = 0
    begin = 0
    end = len(arr) - 1
    odd_sum = 0
    even_sum = 0
    for i in range(0, len(arr), 2):
        even_sum += arr[i]
        odd_sum += arr[i + 1]
    even = True if even_sum > odd_sum else False
    step = 1
    print("*********** THIS IS A GAME **********")
    print(arr)
    while end > begin:
        even = True if even_sum > odd_sum else False
        if odd_sum == even_sum:
            if array[begin] > array[end]:
                even = True if begin % 2 == 0  else False
            else: # array[begin] <= array[end]
                even = True if end % 2 == 0 else False
        print("******* step #", step, "*******")
        print("****** even #", even, ", begin #", begin, ", end #", end, " *****")
        # ***** First player ( Alice ) choice *****
        print(arr[begin:end + 1])
        if (even and begin % 2 == 0) or (even != True and begin % 2 != 0):
            if even:
                even_sum -= array[begin]
            else:
                odd_sum -= array[begin]
            print("ALICE: I take the first:", arr[begin])
            alice_result += arr[begin]
            begin += 1
        else:
            if even:
                even_sum -= array[end]
            else:
                odd_sum -= array[end]
            print("ALICE: I take the last:", arr[end])
            alice_result += arr[end]
            end -= 1
        # ***** Second player ( Bob ) choice *****
        print(arr[begin:end + 1])
        if arr[begin] > arr[end]:
            print("BOB: I take the first:", arr[begin])
            if begin % 2 == 0:
                even_sum -= array[begin]
            else:
                odd_sum -= array[begin]
            bob_result += arr[begin]
            begin += 1
        else:
            print("BOB: I take the last:", arr[end])
            if end % 2 == 0:
                even_sum -= array[end]
            else:
                odd_sum -= array[end]
            bob_result += arr[end]
            end -= 1
        step += 1
        print("Sum - ALICE:", alice_result, ", BOB:", bob_result)
    print("Congratulations! ALICE =", alice_result, ", BOB =", bob_result)


#########################################################################
 # Greedy: ALICE = 10 , BOB = 10  | OddEven: ALICE = 10 , BOB = 10 | Adaptive: ALICE = 13 , BOB = 7
# array = [1, 3, 6, 1, 3, 6]

# Greedy: ALICE = 15 , BOB = 21   | OddEven: ALICE = 21 , BOB = 15 | Adaptive: ALICE = 21 , BOB = 15
# array = [5, 20, 10, 1]

# Greedy: ALICE = 11 , BOB = 10 | OddEven: ALICE = 11 , BOB = 10 | Adaptive: ALICE = 12 , BOB = 9
# array = [3, 4, 6, 2, 1, 5]

# Greedy: ALICE = 20 , BOB = 26 | OddEven: ALICE = 23 , BOB = 23 | Adaptive: ALICE = 23 , BOB = 23
array = [ 6, 9, 1, 2, 16, 12]

print("Greedy Algorithm:")
GreedyAlgorithm(array)
print("\nEven Odd Algorithm:")
OddEvenAlgorithm(array)
print("\nAdaptive Algorithm:")
AdaptiveAlgorithm(array)
