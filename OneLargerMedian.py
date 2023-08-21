# Median problem

# Case:  Given an unordered array of the random numbers, find one element that is larger than the median
'''
* Optimal solution:
* Given an unordered array of random numbers,
* find element that is larger than the median
* by find max element among first check (64) array's elements
* Complexity: O(check) = O(1)
'''


def greatThenMedian(arr, check):
    '''
    Find a max element in the array
    :param arr: an array of random numbers
    :param check: a number of first elements in the array to test
    :return: a max element in the array
    '''
    max_element = arr[0]
    for i in range(check):
        if max_element < arr[i]:
            max_element = arr[i]
    return max_element


from random import *


def checkMedian():
    count, size, numberFirstElements, numOfTests = 0, 10001, 64, 100
    for i in range(numOfTests):
        # get an integer array of the given size [0,size):
        arr = [randint(0, size) for i in range(size)]  # arr = [int(random()*size) for i in range(size)]
        # get an element that is larger than the median:
        bigger_median = greatThenMedian(arr, numberFirstElements)
        # check result whether is larger or not than the median of the array:
        arr_sorted = sorted(arr)
        if bigger_median < arr_sorted[len(arr_sorted) // 2 + 1]:
            count += 1
    probability = float(count // numOfTests)
    print("Count of mistakes = %d, probability of mistakes = %f" % (count, probability))


#########################################

print("Result of checking the optimal solution for an unordered array of random numbers "
      "to find one element that is larger than the median:")
checkMedian()
