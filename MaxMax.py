'''
   The algorithms search for 2 largest elements of an array.
   Each function returns the number of comparisons
   A=[arr[0], arr[1], . . . ,arr[arr.length]]
   max1 = maximum{A}
   max2 = maximum{A\max1}
   Remark: the start values of max1, max2 must be different.
   Assumptions:
   1) elements of the array are different
   2) array length > 2
'''

import time
import random


def twoMaxTwoLoops(arr):
    '''
    # The function twoMaxTwoLoops searches two largest elements of the an array
    # Two separate loops
    # Complexity: O(n) - 2n-2 comparisons
    :param arr: list
    :return: number comparisons
    '''
    max1, indexMax1, comparisons, = arr[0], 0, 0
    # ********** Step 1 Max1 **********
    for i in range(1, len(arr)):  # comparisons=(n-1)
        comparisons += 1
        if arr[i] > max1:
            max1 = arr[i]
            indexMax1 = i
    # ********** Step 2 Max2 **********
    arr[indexMax1] = arr[-1]
    arr[-1] = max1
    max2, indexMax2, = arr[0], 0
    for i in range(1, len(arr) - 1):  # comparisons=(n-2)
        comparisons += 1
        if arr[i] > max2:
            max2 = arr[i]
            indexMax2 = i
    # ********** Termination **********
    arr[-1] = arr[indexMax1]
    arr[indexMax1] = max1
    comparisons += 1  # comparisons=1
    if indexMax1 == indexMax2:
        indexMax2 = len(arr) - 1

    print("twoMaxTwoLoops: maximum1: arr[", indexMax1, "] =", max1,
          "; maximum2: arr[", indexMax2, "] =", max2)
    
    return comparisons


###########################################################
def twoMaxGreatThanMax1(arr):
    '''
    # The function twoMaxGreatThanMax1 searches two largest elements of the an array
    # the first check is: a[i]>max1
    # Complexity: O(n) - 2n comparisons for a random array
    :param arr: list
    :return: number comparisons
    '''
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    comparisons = len(arr) - 2
    for i in range(2, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        else:
            comparisons += 1
            if arr[i] > max2:
                max2 = arr[i]
    print("\ntwoMaxGreatThanMax1 (first, checking max1): max1 =", max1, ", max2 =", max2)
    return comparisons


###########################################################
def twoMaxGreatThanMax2(arr):
    '''
    # The function twoMaxGreatThanMax2 searches two largest elements of the an array
    # the first check is: a[i]>max2
    # Complexity: O(n) - n comparisons for a random array
    :param arr: list
    :return: number comparisons
    '''
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    comparisons = len(arr) - 2
    for i in range(2, len(arr)):
        if arr[i] > max2:
            comparisons += 1
            if arr[i] < max1:
                max2 = arr[i]
            else:
                max2 = max1
                max1 = arr[i]
    print("\ntwoMaxGreatThanMax2 (first, checking max2): max1 =", max1, ", max2 =", max2)
    return comparisons


###########################################################
def twoMaxPairs1(arr):
    '''
    # The function twoMaxPairs1 searches two largest elements of the an array
    # Pair comparisons - the first check is: a[i]>max1
    # Complexity: O(n) - (3/2)*n comparisons
    :param arr: list
    :return: number comparisons
    '''
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    comparisons = 0
    for i in range(2, len(arr) - 1, 2):
        comparisons += 1
        if arr[i] > arr[i + 1]:
            comparisons += 1
            if arr[i] > max1:
                # max2 = max(max1, arr[i+1])
                comparisons += 1
                max2 = max1 if max1 > arr[i + 1] else arr[i + 1]
                max1 = arr[i]
            else:
                comparisons += 1
                if arr[i] > max2:
                    max2 = arr[i]
        else:
            comparisons += 1
            if arr[i + 1] > max1:
                # max2 = max(max1, arr[i])
                comparisons += 1
                max2 = max1 if max1 > arr[i] else arr[i]
                max1 = arr[i + 1]
            else:
                comparisons += 1
                if arr[i + 1] > max2:
                    max2 = arr[i + 1]

    # if number of elements is odd, we check the last element
    comparisons += 1
    if len(arr) % 2 != 0:
        comparisons += 1
        if arr[-1] > max1:
            max2 = max1
            max1 = arr[-1]
        else:
            comparisons += 1
            if arr[-1] > max2:
                max2 = arr[-1]

    print("\ntwoMaxPairs1 (first, checking max1): max1 =", max1, ", max2 =", max2)
    return comparisons


###########################################################

def twoMaxPairs2(arr):
    '''
    # The function twoMaxPairs1 searches two largest elements of the an array
    # Pair comparisons - the first check is: a[i]>max2
    # Complexity: O(n) - (3/2)*n comparisons
    :param arr: list
    :return: number comparisons
    '''
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    comparisons = 0
    for i in range(2, len(arr) - 1, 2):
        comparisons += 1
        if arr[i] > arr[i + 1]:
            comparisons += 1
            if arr[i] > max2:
                comparisons += 1
                if arr[i] > max1:
                    comparisons += 1
                    max2 = max1 if max1 > arr[i + 1] else arr[i + 1]
                    max1 = arr[i]
                else:
                    max2 = arr[i]
        else:
            comparisons += 1
            if arr[i + 1] > max2:
                comparisons += 1
                if arr[i + 1] > max1:
                    comparisons += 1
                    max2 = max1 if max1 > arr[i] else arr[i]
                    max1 = arr[i + 1]
                else:
                    max2 = arr[i + 1]

    # if number of elements is odd, we check the last element
    comparisons += 1
    if len(arr) % 2 != 0:
        comparisons += 1
        if arr[-1] > max1:
            max2 = max1
            max1 = arr[-1]
        else:
            comparisons += 1
            if arr[-1] > max2:
                max2 = arr[-1]

    print("\ntwoMaxPairs2 (first, checking max2): max1 =", max1, ", max2 =", max2)
    return comparisons


###########################################################
import sys


# The function twoMaxRecurs searches two largest elements of the an array
# Recursion - Binary Tree & Stack (Stack by Array)
# Complexity: log(n) + (n-1) comparisons
def twoMaxRecurs(arr):
    ans = twoMaxRecursHelp(arr, 0, len(arr))
    print("\ntwoMaxRecurs: max1 =", ans[0], ", max2 =", ans[1])
    return ans[2]


def twoMaxRecursHelp(arr, low, high):
    if int(high) == (int(low) + 2):
        max1 = arr[low]
        max2 = arr[low + 1]
        if max1 < max2:
            max1 = arr[low + 1]
            max2 = arr[low]
        maxArray = [max1, max2, 1]
        return maxArray
    elif int(high) == (int(low) + 1):
        max1 = arr[low]
        maxArray = [max1, -sys.maxsize - 1, 0]
        return maxArray
    else:
        mid = (low + high) // 2
        mL = twoMaxRecursHelp(arr, low, mid)  # [low, mid)
        mH = twoMaxRecursHelp(arr, mid, high)  # [mid, high)
        # maxArray[0] = max1, maxArray[1] = max2, maxArray[2] = comparisons
        maxArray = [0] * 3
        comp = mL[2] + mH[2]
        i, j, = 0, 0
        comp += 1
        if mL[i] > mH[j]:
            maxArray[0] = mL[i]
            i += 1
        else:
            maxArray[0] = mH[j]
            j += 1
        comp += 1
        maxArray[1] = mL[i] if mL[i] > mH[j] else mH[j]
        maxArray[2] = comp
        return maxArray


###########################################################
###########################################################
def createList(size=10000):
    lst = [random.randint(0, size) for i in range(0, size)]  # [int(random.random()*(size)) for i in range(0, size)]
    return lst


# Prints an average time and an average number of comparisons for all methods
def checkTimesRandomArray():
    size_list = 100001
    num_iteration = 64
    diff = [0] * 6
    comparisons = [0] * 6
    print("size_list =", size_list, ";  num_iteration =", num_iteration)
    for i in range(num_iteration):
        arr = createList(size_list)

        # twoMaxTwoLoops - number of comparisons
        start = time.time()
        comparisons[0] += twoMaxTwoLoops(arr)
        end = time.time()
        diff[0] += (end - start)

        # twoMaxGreatThanMax1 - number of comparisons
        start = time.time()
        comparisons[1] += twoMaxGreatThanMax1(arr)
        end = time.time()
        diff[1] += (end - start)

        # twoMaxGreatThanMax2 - number of comparisons
        start = time.time()
        comparisons[2] += twoMaxGreatThanMax2(arr)
        end = time.time()
        diff[2] += (end - start)

        # twoMaxPairs1 - number of comparisons
        start = time.time()
        comparisons[3] += twoMaxPairs1(arr)
        end = time.time()
        diff[3] += (end - start)

        # twoMaxPairs2 - number of comparisons
        start = time.time()
        comparisons[4] += twoMaxPairs2(arr)
        end = time.time()
        diff[4] += (end - start)

        # twoMaxRecurs - number of comparisons
        start = time.time()
        comparisons[5] += twoMaxRecurs(arr)
        end = time.time()
        diff[5] += (end - start)

    for i in range(len(diff)):
        if i == 0:
            name_alg = "twoMaxTwoLoops"
        elif i == 1:
            name_alg = "twoMaxGreatThanMax1"
        elif i == 2:
            name_alg = "twoMaxGreatThanMax2"
        elif i == 3:
            name_alg = "twoMaxPairs1"
        elif i == 4:
            name_alg = "twoMaxPairs2"
        elif i == 5:
            name_alg = "twoMaxRecurs"
        else:
            name_alg = ""

    print(f"{name_alg} Algorithm: average number of comparisons =", comparisons[i] / num_iteration,
          "==> average time =", diff[i] / num_iteration)


###########################################################
#  Measuring the execution time of the code by using an in-built python library 'timeit':
'''
The module function 'timeit.timeit(stmt, setup, timer, number)' accepts four arguments: 
    'stmt' which is the statement to measure; it defaults to ‘pass’.
    'setup' which is the code that you run before running the stmt; it defaults to ‘pass’. 
     (for example, import the required modules for the code.)
    'timer' which is a timeit.Timer object; 
    'number' which is the number of executions of the 'stmt'.
the timeit.timeit() function returns the number of seconds it took to execute the code.
'''

import timeit


def twoMaxTwoLoops_random_time():
    twoMaxTwoLoops(arr_random)


def twoMaxTwoLoops_ascending_time():
    twoMaxTwoLoops(arr_sorted_ascending)


def twoMaxTwoLoops_descending_time():
    twoMaxTwoLoops(arr_sorted_descending)


'''
Get maximum and minimum values of int using sys.maxsize in Python3\
import sys
# Get maximum integer value
print(sys.maxsize)
Syntax to get minimum int:
-sys.maxsize - 1
'''
###########################################################
if __name__ == "__main__":
    size = 10 ** 5  # length of list
    a = [7, 3, 4, 9, 0, 3]
    a = createList(size)
    print("twoMaxTwoLoops - number of comparisons:", twoMaxTwoLoops(a))
    print("twoMaxGreatThanMax1 - number of comparisons:", twoMaxGreatThanMax1(a))
    print("twoMaxGreatThanMax2 - number of comparisons:", twoMaxGreatThanMax2(a))
    print("twoMaxPairs1 - number of comparisons:", twoMaxPairs1(a))
    print("twoMaxPairs2 - number of comparisons:", twoMaxPairs2(a))
    print("twoMaxRecurs - number of comparisons:", twoMaxRecurs(a))

    # checkTimesRandomArray()

    arr_random = createList(size)
    arr_sorted_ascending = sorted(arr_random)  # Default is False (sorts ascending)
    arr_sorted_descending = sorted(arr_random, reverse=True)  # True sorts descending

    '''
    ######### Check twoMaxTwoLoops ##########
    iterations = 64  # number of iterations to timeit
    t1 = timeit.timeit(twoMaxTwoLoops_random_time, number=iterations)
    print('Average time twoMaxTwoLoops for random array: {}'.format(float(t1/iterations)))

    t1 = timeit.timeit(twoMaxTwoLoops_ascending_time, number=iterations)
    print('Average time twoMaxTwoLoops for ascending array: {}'.format(float(t1/iterations)))

    t1 = timeit.timeit(twoMaxTwoLoops_descending_time, number=iterations)
    print('Average time twoMaxTwoLoops for descending array: {}'.format(float(t1/iterations)))

    '''
