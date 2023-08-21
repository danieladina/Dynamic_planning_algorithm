'''
Finding the smallest and largest elements in the array
(with the least number of comparisons)
'''
import time
import random


# standard algorithm with Two Loops for search of maximum && minimum elements:
# Complexity: O(n) = (2n - 2) - 2n comparisons
def minMaxTwoLoops(arr):
    comparisons = 0
    minimum = arr[0]
    for i in arr[1:]:  # O(n) = n-1
        comparisons += 1
        if i < minimum:
            minimum = i
    maximum = arr[0]
    for i in arr[1:]:  # O(n) = n-1
        comparisons += 1
        if i > maximum:
            maximum = i
    print("min= ", minimum, ", max =", maximum)
    return int(comparisons)


# Prints an average time and an average number of comparisons in two loops algorithm
def meanNumOfComparisonsTwoLoops(size=10000, num_iteration=10):
    comparisons = 0
    diff = 0
    for i in range(num_iteration):
        lst = createList(size)
        start = time.time()
        comparisons += minMaxTwoLoops(lst)
        end = time.time()
        diff += (end - start)
    print("minMaxTwoLoops:")
    print("Average time minMaxTwoLoops:", float(diff / num_iteration), "in sec.")
    print("Average number of comparisons:", float(comparisons / num_iteration))


###########################################################
# standard algorithm with One Loop for search of maximum && minimum elements:
# Complexity: O(n) - 2n comparisons:
#  Worst case: O(n) = 2n-2, when the list is sorted in the ascending order.
#  Best case : O(n) = n-1 , when the list is sorted in the descending order.
def minMaxStandard(arr):
    comparisons = 0
    minimum, maximum = arr[0], arr[0]
    for i in range(1, len(arr)):
        comparisons += 1
        if i < minimum:
            minimum = i
        else:
            comparisons += 1
            if i > maximum:
                maximum = i
    print("min= ", minimum, ", max =", maximum)
    return int(comparisons)


# Prints an average time and an average number of comparisons in standard algorithm
def meanNumOfComparisonsStandard(size=10000, num_iteration=10):
    comparisons = 0
    diff = 0
    for i in range(num_iteration):
        lst = createList(size)
        start = time.time()
        comparisons += minMaxStandard(lst)
        end = time.time()
        diff += (end - start)
    print("minMaxStandard:")
    print("Average time minMaxTwoLoops:", float(diff / num_iteration), "in sec.")
    print("Average number of comparisons:", float(comparisons / num_iteration))


###########################################################
###########################################################
# Search of maximum && minimum elements by pairs:
# Complexity: O(n) - 1.5*n comparisons
def minMaxPairs(arr):
    comparisons = 0
    maximum = arr[1] if arr[0] < arr[1] else arr[0]
    minimum = arr[0] if arr[0] < arr[1] else arr[1]

    for i in range(2, len(arr) - 1, 2):
        comparisons += 1
        if arr[i] < arr[i + 1]:
            comparisons += 2
            if arr[i] < minimum:
                minimum = arr[i]
            if arr[i + 1] > maximum:
                maximum = arr[i + 1]
        else:
            comparisons += 2
            if arr[i + 1] < minimum:
                minimum = arr[i + 1]
            if arr[i] > maximum:
                maximum = arr[i]

    # if number of elements is odd, we check the last element
    if len(arr) % 2 != 0:
        comparisons += 1
        if arr[len(arr) - 1] > maximum:
            maximum = arr[len(arr) - 1]
        else:
            comparisons += 1
            if arr[len(arr) - 1] < minimum:
                minimum = arr[len(arr) - 1]

    print("min= ", minimum, ", max =", maximum)
    return int(comparisons)


# Prints an average time and an average number of comparisons in standard algorithm
def meanNumOfComparisonsPairs(size=10000, num_iteration=10):
    comparisons = 0
    diff = 0
    for i in range(num_iteration):
        lst = createList(size)
        start = time.time()
        comparisons += minMaxPairs(lst)
        end = time.time()
        diff += (end - start)
    print("minMaxPairs:")
    print("Average time minMaxTwoLoops:", float(diff / num_iteration), "in sec.")
    print("Average number of comparisons:", float(comparisons / num_iteration))


def createList(size=10000):
    lst = [random.randint(0, size) for i in
           range(0, size)]  # [int(random.random()*(size)) for i in range(0, size)]
    return lst


def test_all_algs():
    size, num_iteration = 100001, 10
    print("size_list =", size, ", num_iteration =", num_iteration)
    lst = createList(size)
    print("len =", len(lst))
    print("Random list:")
    print("TwoLoops: number of comparisons is", minMaxTwoLoops(lst))
    print("Standard: number of comparisons is", minMaxStandard(lst))
    print("minMaxPairs: number of comparisons is", minMaxPairs(lst))

    lst.sort()
    print("\nSorted list in the ascending order:")
    print("TwoLoops: number of comparisons is", minMaxTwoLoops(lst))
    print("Standard: number of comparisons is", minMaxStandard(lst))
    print("minMaxPairs: number of comparisons is", minMaxPairs(lst))

    lst.sort(reverse=True)
    print("\nSorted list in the descending order:")
    print("TwoLoops: number of comparisons is", minMaxTwoLoops(lst))
    print("Standard: number of comparisons is", minMaxStandard(lst))
    print("minMaxPairs: number of comparisons is", minMaxPairs(lst))

    #print("Random list - Average:")
    # meanNumOfComparisonsTwoLoops(size, num_iteration)
    # meanNumOfComparisonsStandard(size, num_iteration)
    # meanNumOfComparisonsPairs(size, num_iteration)


def main():
    size, num_iteration = 100001, 10
    diff = [0] * 3
    comparisons = [0] * 3
    print("size_list =", size, ", num_iteration =", num_iteration)
    for i in range(num_iteration):
        lst = createList(size)

        start = time.time()
        comparisons[0] += minMaxTwoLoops(lst)
        end = time.time()
        diff[0] += (end - start)

        start = time.time()
        comparisons[1] += minMaxStandard(lst)
        end = time.time()
        diff[1] += (end - start)

        start = time.time()
        comparisons[2] += minMaxPairs(lst)
        end = time.time()
        diff[2] += (end - start)

    for i in range(len(diff)):
        if i == 0:
            name_alg = "TwoLoops"
        elif i == 1:
            name_alg = "Standard"
        elif i == 2:
            name_alg = "Pairs"
        else:
            name_alg = ""
        print(f"{name_alg} Algorithm: average number of comparisons =", comparisons[i] / num_iteration,
              "==> average time =", diff[i] / num_iteration)


###########################################################
if __name__ == "__main__":
    test_all_algs()
    # main()
