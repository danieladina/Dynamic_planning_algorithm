'''
 * Full/Exhaustive Search algorithm
 * LCS - Longest Common Substring
 * returns the LCS of X and Y
'''


def plus1(arr):
    '''
    * Building Help/Musk array containing a serial binary number from 0 to 111 ... 11
	* size of a help array is according to the length's sequence
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


import math


def checkPlus1():
    n = 4
    count = int(math.pow(2, n))
    arr = [0] * n
    print(arr)
    for i in range(count):
        plus1(arr)
        print(arr)


def allCombinations(X):
    '''
    * Find all subsequences in the sequence
	* Complexity: O(2^n), n=X.length()
    :param X: the sequence
    :return: list of all subsequences in the sequence
    '''
    n = len(X)
    count = int(math.pow(2, n)) - 1
    list_all = [] * count
    bin_list = [0] * n
    for i in range(count):
        plus1(bin_list)
        # print(bin_list)
        temp = ""
        for j in range(n):
            if bin_list[j] == 1:
                temp += X[j]
        # print(temp)
        list_all.insert(i, temp)
    return list_all


def checkAllCombinations():
    list_check = ["ab", "abc", "abcd"]
    for i in list_check:
        lst_bn = allCombinations(i)
        print(lst_bn)


def exhaustiveSearch(XX, YY):
    '''
    * The Exhaustive Search Algorithm of LCS
	* Complexity: O(2^n * 2^m * min(m,n)) = O(2^(m+n) * min(m,n))
    :param XX: the first string
    :param YY: the second string
    :return: string which contains the longest common sequence
    '''
    ans, maxLen,  = "", 0
    X, Y, = XX, YY  # X is the shortest string, Y is the longer string
    if len(XX) > len(YY):
        Y = XX
        X = YY
    X_ALL, Y_ALL, = [], []
    X_ALL = allCombinations(X)
    Y_ALL = allCombinations(Y)
    for i in range(len(X_ALL)):
        len_ = len(X_ALL[i])
        for j in range(len(Y_ALL)):
            if X_ALL[i] == Y_ALL[j] and len_ > maxLen:
                maxLen = len_
                ans = X_ALL[i]
    return ans

def checkExhaustiveSearch():
    print("Check Greedy algorithms:")
    listTwoStr = [["abcbdab", "bdcaba"],
                  ["abcd", "acd"],
                  ["cdbac", "abdbb"],
                  ["abcabdc", "abcbdcbad"],
                  ["abcabdc", "xyz"],
                  ["acccccccb", "bccccccca"]]

    for i in range(len(listTwoStr)):
        print(f"LCS({listTwoStr[i][0]},{listTwoStr[i][1]}) is ", exhaustiveSearch(listTwoStr[i][0], listTwoStr[i][1]))
########################
# checkPlus1()
# checkAllCombinations()
checkExhaustiveSearch()
