'''
Longest Increasing Subsequence - LIS
'''

'''
 * Solution 1: The Greedy Algorithm
 * Complexity: O(n)
'''


def LIS_Greedy(arr):
    '''
    * The Greedy Algorithm for LIS
    * Complexity: O(n)
    :param arr: number sequence
    :return: increasing sequence
    '''
    if len(arr) <= 0:
        return []
    res = [arr[0]]
    k = 0
    for i in range(1, len(arr)):
        if arr[i] > res[k]:
            k += 1
            res.insert(k, arr[i])
    return res


'''
 * Solution 2: The Full Search Algorithm - Exhaustive Search 
 * Complexity: O(2^n*n)
'''


from math import pow
# First Version of the Solution for The Full Search Algorithm - Exhaustive Search
def LIS_ExhaustiveSearch(arr):
    '''
    * Solution 2.1 (First Version): The Full Search Algorithm - Exhaustive Search
    * Complexity: O(2^n*n)
    :param arr: number sequence
    :return: increasing sequence
    '''
    count = int(pow(2, len(arr))) - 1
    # Declare the list (array) for all binary subsequences and initialize it
    bin_list = [0] * len(arr)
    ans = []
    max_len = 0
    for i in range(count):
        plus1(bin_list)  # Step 1: Build a array of all binary subsequences - O(n)
        # print(bin_list)
        temp = []
        k = 0
        flag = True
        j = 0
        while flag and j < len(arr):  # //Step 2: Build a array of all increasing subsequences - O(n)
            if bin_list[j] == 1:  # copy elements with value '1' in the binary array to temp list
                if k >= 1:  # check if it's increasing
                    if temp[k - 1] < arr[j]:
                        temp.insert(k, arr[j])
                        k += 1
                    else:
                        flag = False
                else:
                    temp.insert(k, arr[j])
                    k += 1
            if flag:  # Step 3: Find a length of LIS
                if k > max_len:
                    ans = temp  # Step 4: Build a array of a longest increasing subsequences.
                    max_len = k
            j += 1
    return ans


def plus1(arr):
    '''
    * Help Function for LIS_ExhaustiveSearch:
    * Build a mask binary array of all subsequences
    * Complexity: O(n)
    :param arr: array that containing a serial binary number before addind one bit
    :return: array containing a serial binary number after addind one bit
    '''
    i = len(arr) - 1
    while i >= 0 and arr[i] == 1:
        arr[i] = 0
        i -= 1
    if i >= 0:
        arr[i] = 1


# Second Version of the Solution for The Full Search Algorithm - Exhaustive Search
def exhaustiveSearch(arr):
    '''
    * Solution 2.1 (First Version): The Full Search Algorithm - Exhaustive Search
    * Complexity: O(2^n*n)
    :param arr: number sequence
    :return: increasing sequence
    '''
    ans, max_len, = "", 0
    all_sublist = allCombinations(arr)
    for i in range(len(all_sublist)):
        len_ = len(all_sublist[i])
        if isSorted(all_sublist[i]) and len_ > max_len:
            max_len = len_
            ans = all_sublist[i]
    return ans


def isSorted(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True


def allCombinations(X):
    '''
    * Find all subsequences in the sequence
	* Complexity: O(2^n), n=X.length()
    :param X: the sequence
    :return: list of all subsequences in the sequence
    '''
    n = len(X)
    count = int(pow(2, n)) - 1
    list_all = [] * count
    bin_list = [0] * n
    for i in range(count):
        plus1(bin_list)
        # print(bin_list)
        temp = []
        for j in range(n):
            if bin_list[j] == 1:
                temp.append(X[j])
        # print(temp)
        list_all.insert(i, temp)
    return list_all


def checkAllCombinations():
    list_check = [[1, 2, 3],
                  [8, 1, 100, 101, 2],
                  [3, 2, 1, 0]]
    for i in list_check:
        lst_bn = allCombinations(i)
        print(lst_bn)


'''
 * Solution 3: Algorithm that uses the LCS for number arrays instead of string arrays
 * Complexity: O(n^2) + O(nlogn) =  O(n^2)
'''


def LIS_with_LCS(arr):
    '''
    * Algorithm that uses the LCS for for number arrays instead of string arrays
    * Complexity: O(n^2) + O(nlogn) =  O(n^2)
    :param arr: number sequence
    :return: increasing sequence
    '''
    arr_sorted = sorted(arr)
    return lcsMaxSequence(arr, arr_sorted)


def lcsMaxSequence(s1, s2):
    matrix = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    seq_length = matrix[len(matrix) - 1][len(matrix[0]) - 1]
    result = [0] * seq_length
    i = len(matrix) - 1
    j = len(matrix[0]) - 1
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result[seq_length - 1] = s1[i - 1]
            seq_length -= 1
            i -= 1
            j -= 1
        elif matrix[i - 1][j] > matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return result


'''
 * Solution 4: Dynamic Programming of LIS
 * Step 4.1:
 * Calculation of a length of the Longest Increasing subsequence
 * Complexity: O(n*logn)
'''


def LIS_DF_Length(arr):
    '''
    * Calculation of a length of the Longest Increasing subsequence
    * Complexity: O(n*logn)
    :param arr: sequence
    :return: length of the Longest Increasing subsequence
    '''
    t = [0] * len(arr)
    t[0] = arr[0]
    lis = 0
    for i in range(1, len(arr)):
        index = binarySearchBetween(t, lis, arr[i])
        t[index] = arr[i]
        if index > lis:
            lis += 1
    return lis + 1


'''
 * Help Function for LIS_DF_Length:
 * Binary search between in array
 * Complexity: O(logn)
'''


def binarySearchBetween(arr, end, value):
    '''
    * Binary search between in array:
    if value<arr[0] the function returns zero
    if value>arr[end] the function returns end+1
    if arr[index-1] < value < arr[index] the function returns index
    * Complexity: O(logn)
    :param arr: array for search
    :param end: last index for search
    :param value: value for search
    :return: index in the array for the value
    '''
    low, high = 0, end
    if value < arr[0]:
        return 0
    if value > arr[end]:
        return end + 1
    while low <= high:
        middle = (low + high) // 2
        if low == high:  # stop search
            return low
        else:
            if arr[middle] == value:  # value was found
                return middle
            if value < arr[middle]:  # value is supposed in the left
                high = middle
            else:  # value is supposed in the right
                low = middle + 1
    return -1


'''
 * Solution 4: Dynamic Programming of LIS
 * Step 4.2: Get the Longest Increasing subsequence
 * Complexity: O(n*logn+n^2)=O(n^2)
'''


def LIS_DF(arr):
    '''
    * Get the Longest Increasing subsequence
    * Complexity: O(n*logn+n^2)=O(n^2)
    :param arr: sequence
    :return: Longest Increasing subsequence
    '''
    # mat = [[0 for x in range(len(arr))] for x in range(len(arr))]
    mat = [[0] * len(arr) for x in range(len(arr))]
    mat[0][0] = arr[0]
    end = 0
    for i in range(1, len(arr)):
        index = binarySearchBetweenMat(mat, end, arr[i])
        for j in range(index):
            mat[index][j] = mat[index - 1][j]
        mat[index][index] = arr[i]
        if index > end:
            end += 1

    ans = mat[end][0:end + 1]
    return ans


'''
 * Help Function for LIS_DF:
 * Binary search between on the diagonal of a matrix
'''


def binarySearchBetweenMat(mat, end, value):
    '''
    * Binary search between in the diagonal of the matrix
    * Complexity: O(logn)
    :param mat: a matrix for search
    :param end: a last index for search
    :param value: a value for search
    :return: index in the diagonal of the matrix
    '''
    low, high = 0, end
    if value < mat[0][0]:
        return 0
    if value > mat[end][end]:
        return end + 1
    while low <= high:
        middle = (low + high) // 2
        if low == high:  # stop search
            return low
        else:
            if mat[middle][middle] == value:  # value was found
                return middle
            if value < mat[middle][middle]:  # value is supposed in the left
                high = middle
            else:  # value suppose is supposed in the right
                low = middle + 1
    return -1


#######################################################################
#######################################################################
def checkLIS_Greedy():
    print("Check LIS_Greedy algorithm:")
    check_lists = [[1, 2, 3],
                   [8, 1, 100, 101, 2],
                   [3, 2, 1, 0],
                   [-3, -2, 101, 9, 10, 11, 1, 2, 3, 100, 4, -1, 5, 6],
                   [8, 2, 9, 3, 1, 10, 4, 6, 5, 7]]

    for i in range(len(check_lists)):
        print(f"LIS({check_lists[i]}) is ", LIS_Greedy(check_lists[i]))


def checkExhaustiveSearch():
    print("Check Exhaustive Search algorithm (first version):")
    check_lists = [[1, 2, 3],
                   [8, 1, 100, 101, 2],
                   [3, 2, 1, 0],
                   [-3, -2, 101, 9, 10, 11, 1, 2, 3, 100, 4, -1, 5, 6],
                   [8, 2, 9, 3, 1, 10, 4, 6, 5, 7]]

    for i in range(len(check_lists)):
        print(f"LIS({check_lists[i]}) is ", LIS_ExhaustiveSearch(check_lists[i]))


def checkExhaustiveSearch_():
    print("Check Exhaustive Search algorithm (second version):")
    check_lists = [[1, 2, 3],
                   [8, 1, 100, 101, 2],
                   [3, 2, 1, 0],
                   [-3, -2, 101, 9, 10, 11, 1, 2, 3, 100, 4, -1, 5, 6],
                   [8, 2, 9, 3, 1, 10, 4, 6, 5, 7]]

    for i in range(len(check_lists)):
        print(f"LIS({check_lists[i]}) is ", exhaustiveSearch(check_lists[i]))


def checkLIS_with_LCS():
    print("Check LIS_with_LCS algorithm:")
    check_lists = [[1, 2, 3],
                   [8, 1, 100, 101, 2],
                   [3, 2, 1, 0],
                   [-3, -2, 101, 9, 10, 11, 1, 2, 3, 100, 4, -1, 5, 6],
                   [8, 2, 9, 3, 1, 10, 4, 6, 5, 7]]

    for i in range(len(check_lists)):
        print(f"LIS({check_lists[i]}) is ", LIS_with_LCS(check_lists[i]))


def checkLIS_DF_Length():
    print("Check LIS_DF_Length algorithm:")
    check_lists = [[3],
                   [1, 3],
                   [1, 2, 2, 3, 3],
                   [1, 2, 3],
                   [8, 1, 100, 101, 2],
                   [3, 2, 1, 0],
                   [-3, -2, 101, 9, 10, 11, 1, 2, 3, 100, 4, -1, 5, 6],
                   [8, 2, 9, 3, 1, 10, 4, 6, 5, 7]]

    for i in range(len(check_lists)):
        print(f"Length of LIS({check_lists[i]}) is ", LIS_DF_Length(check_lists[i]))


def checkLIS_DF():
    print("Check LIS_DF algorithm:")
    check_lists = [[3],
                   [1, 3],
                   [1, 2, 2, 3, 3],
                   [1, 2, 3],
                   [8, 1, 100, 101, 2],
                   [3, 2, 1, 0],
                   [-3, -2, 101, 9, 10, 11, 1, 2, 3, 100, 4, -1, 5, 6],
                   [8, 2, 9, 3, 1, 10, 4, 6, 5, 7]]

    for i in range(len(check_lists)):
        print(f"LIS({check_lists[i]}) is ", LIS_DF(check_lists[i]))


#######################################################################
#######################################################################
# checkLIS_Greedy()
# checkAllCombinations()
# checkExhaustiveSearch()
# checkExhaustiveSearch_()
checkLIS_with_LCS()
checkLIS_DF_Length()
checkLIS_DF()

