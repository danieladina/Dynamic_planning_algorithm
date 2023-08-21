'''
Two sum problem of Given List:
find the pair of the two indexes from the given list whose sum of these elements is equal to the given target value.
We can assume that the array has only one pair of integers that add up to the target sum.
First, a given list or array must be sorted in increasing manner.
'''


# Approach by Using Two Pointers:
'''
We will use the binary search algorithm where the given list array must be sorted.
We will use the two pointers: left and right;
the left denotes the first element, and the right denotes the last element of the list.
Then we compare the sum of the pointer's value to the target value; if some of the value and target is equal, return the pointers index pairs.
If the sum of value is more than the target, we decrement the right pointer.
Otherwise, some of the value is less than the target; we need to increase the left pointer by one and check the same conditions.
'''
def twoSumTwoPointers(arr, target):
    '''
    The time complexity will be O(n) even in the worst case, we visit all the elements in the array only once.
    :param arr: number list that sorted in increasing manner
    :param target: target value
    :return: find the pair of the two indexes from the given list whose sum of these elements is equal to the given target value.
    '''
    left = 0
    right = len(arr) - 1
    temSum = 0
    while (left < right):
        tempSum = arr[left] + arr[right]
        if tempSum == target:
            return list((left, right))
        elif tempSum > target:
            right -= 1
        elif tempSum < target:
            left += 1
    return list((-1, -1))

# Approach by Brute Force Approach:
'''
This ia a primary goal to solve this problem, not efficiently.
We check every possible pair and the number of possible pairs in the array.
We will use the two for loop, add the two values, and compare the target value.
If it is equal to the target value, return the indices of pairs of the integer.
'''
def twoSumBruteForce(arr, target):
    '''
    The time complexity is O(n*n):
    The first for loop visits n numbers of elements and second for loop visits n-1.
    Hence, the check for the possible and total number of pair are: n*(n-1)/2
    :param arr: number list that sorted in increasing manner
    :param target: target value
    :return: find the pair of the two indexes from the given list whose sum of these elements is equal to the given target value.
    '''
    length = len(arr)
    for i in range(length - 1):  # Run the first loop to point the first index of the solution in the array.
        for j in range(i + 1, length): # Run another loop to point a second index of the solution for every first integer.
            if arr[i] + arr[j] == target: #  the both elements equal to the target value, return the both indices values
                new_list = i, j
                return list(new_list)
    return -1

if __name__ == '__main__':

    list_1 = [2, 7, 11, 15]
    print(list_1)
    num = 26
    print("Two Pointers Solution: for target value =",num , ", two indexes in the list are", twoSumTwoPointers(list_1, num))
    print("Brute Force Solution: for target value =",num , ", two indexes in the list are", twoSumTwoPointers(list_1, num))
    num = 18
    print("\nTwo Pointers Solution: for target value =", num, ", two indexes in the list are", twoSumTwoPointers(list_1, num))
    print("Brute Force Solution: for target value =",num , ", two indexes in the list are", twoSumTwoPointers(list_1, num))
    num = 56
    print("\nTwo Pointers Solution: for target value =", num, ", two indexes in the list are", twoSumTwoPointers(list_1, num))
    print("Brute Force Solution: for target value =",num , ", two indexes in the list are", twoSumTwoPointers(list_1, num))

