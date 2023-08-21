'''
 * Dynamic Programming implementation of LCS problem:
 * LCS - Longest Common Subsequence
 * returns the LCS of X and Y
'''


def LCS_Matrix(X, Y):
    '''
    Creating matrix of length common subsequences
    L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    Complexity: O(m*n) in worst case, O(m+n), assuming the size of the alphabet is constant.
    :param X: first sequence
    :param Y: second sequence
    :return: a matrix of length common subsequences
    '''
    # finding the length of the strings:
    m = len(X)  # number of rows
    n = len(Y)  # number of columns
    # creating the matrix for storing the dp values:
    L = [[None] * (n + 1) for i in range(m + 1)]

    #Following steps for building L[m + 1][n + 1] from upper to bottom:
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0  # first row and first column
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L, L[m][n]


def lcsMaxLength(X, Y):
    '''
    Getting a length of longest common subsequence
    :param X: first sequence
    :param Y: second sequence
    :return: a length of longest common subsequence
    '''
    return LCS_Matrix(X, Y)[1]


def lcsMaxSequence(X, Y):
    seqLength = LCS_Matrix(X, Y)[1]
    matrix_lcs = LCS_Matrix(X, Y)[0]
    maxSeq, count, = "", seqLength - 1
    i = len(X)
    j = len(Y)
    while count >= 0:
        if X[i-1] == Y[j-1]:
            maxSeq = X[i-1] + maxSeq
            i -= 1
            j -= 1
            count -= 1
        elif matrix_lcs[i][j] == matrix_lcs[i][j-1]:
            j -= 1
        else:
            i -= 1

    return maxSeq

def checkLengthLCS():
    print("Check Length of the Longest Common Subsequence in the Dynamic algorithm:")
    listTwoStr = [["abcbdab", "bdcaba"],
                  ["abcd", "acd"],
                  ["cdbac", "abdbb"],
                  ["abcabdc", "abcbdcbad"],
                  ["abcabdc", "xyz"],
                  ["acccccccb", "bccccccca"]]

    for i in listTwoStr:
        print(f"LCS({i[0]},{i[1]}) is", lcsMaxLength(i[0], i[1]))


def checkMaxSequenceLCS():
    print("Check Max Subsequence of the Longest Common Subsequence in the Dynamic algorithm:")
    listTwoStr = [["abcbdab", "bdcaba"],
                  ["abcd", "acd"],
                  ["cdbac", "abdbb"],
                  ["abcabdc", "abcbdcbad"],
                  ["abcabdc", "xyz"],
                  ["acccccccb", "bccccccca"]]

    for i in listTwoStr:
        print(f"LCS({i[0]},{i[1]}) is", lcsMaxSequence(i[0], i[1]))
################################
#checkLengthLCS()
checkMaxSequenceLCS()
