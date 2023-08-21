'''
Finding the largest subsequence that consists the ones only
'''


def subSqOf1(arr):
    '''
    Dynamic algorithm: using a help array
    Complexity: O(n)
    :param arr: an array
    :return: print a length of the largest subsequence, indexes of interval
    '''
    # help array for storing a number of ones in the interval that ends at i:
    h = [0 for i in range(0, len(arr))]  #[0] * len(arr)
    h[0] = arr[0]
    ind_max = 0
    for i in range(1, len(h)):
        if arr[i] == 1:
            h[i] = h[i - 1] + 1
    #print("Help array in the Dynamic:", h, end="")
    # finding an index of the element with a maxLengh:
    for i in range(1, len(h)):
        if h[i] > h[ind_max]:
            ind_max = i
    max_len = int(h[ind_max])
    ind_begin = int(ind_max) - max_len + 1
    print("Dynamic: max_len =", max_len, ", indexBegin =", ind_begin)


def subSqOf1Standard(arr):
    '''
    Standard algorithm: Improved greedy algorithm
    Complexity: O(n)
    :param arr: an array
    :return: print a length of the largest subsequence, indexes of interval
    '''
    count, max_len, ind_begin = 0, 0, 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            if count > max_len:
                max_len = count
                ind_begin = i - count
            count = 0
    # tail processing:
    if count > max_len:
        max_len = count
        ind_begin = len(arr) - count
    print("Standard: max_len =", max_len, ", indexBegin =", ind_begin)

def test_all_algs():
    list_sequences = [[1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
                     [1, 0, 1],
                     [1, 0, 1, 1, 1, 0],
                     [1, 0, 1, 1, 1],
                     [1, 0, 1, 1, 1, 0, 1, 1]]
    for i in list_sequences:
        print(f"\nFor sequence({i}):")
        subSqOf1Standard(i)
        subSqOf1(i)
###########################################################
test_all_algs()
'''
arr = [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1]
arr1 = [1, 0, 1]
arr2 = [1, 0, 1, 1, 1, 0]
arr3 = [1, 0, 1, 1, 1]
arr4 = [1, 0, 1, 1, 1, 0, 1, 1]
subSqOf1Standard(arr1)
subSqOf1(arr1)

subSqOf1Standard(arr)
subSqOf1(arr)

subSqOf1Standard(arr2)
subSqOf1(arr2)

subSqOf1Standard(arr3)
subSqOf1(arr3)

subSqOf1Standard(arr4)
subSqOf1(arr4)
'''