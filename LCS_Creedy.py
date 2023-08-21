# LCS - Longest Common Substring
'''
 * Greedy algorithms
 * LCS - Longest Common Substring
 * returns the LCS of X and Y
'''

def greedy(XX, YY):
    '''
    The greedy algorithm:
    Complexity: O(m*n),  m=X.length(), n=Y.length()
    :param XX: the first string
    :param YY: the second string
    :return: string which contains the longest common sequence
    '''
    ans, start, i, index, = "", 0, 0, 0
    X, Y, = XX, YY  # X is the shortest string, Y is the longer string
    if len(XX) > len(YY):
        Y = XX
        X = YY
    while i < len(X) and index < len(Y):
        index = Y.find(X[i], start)
        if index != -1:
            ans += X[i]
            start = index + 1
        i += 1
    return ans


def greedyWithHelp(XX, YY):
    '''
    The Greedy Improved Algorithm of LCS
    # associative memory
    Complexity: O(m + n) + O(min(m,n))
    :param XX: the first string
    :param YY: the second string
    :return: string which contains the longest common sequence
    '''
    X, Y, = XX, YY  # X is the shortest string, Y is the longer string
    if len(XX) >= len(YY):
        Y = XX
        X = YY
    help = [0 for i in range(26)]
    for i in range(len(X)):  # O(min(m, n))
        if X[i] != None:
            num_dublicate = X.count(X[i])
            place = ord(X[i]) - ord('a')
            help[place] = num_dublicate
    ans, start, i, index, = "", 0, 0, 0
    while i < len(Y) and index < len(X): # O(m+n)
        place = ord(Y[i]) - ord('a')
        if help[place] > 0:
            index = X.find(Y[i], start)
            if index != -1:
                ans += Y[i]
                start = index + 1
                help[place] -= 1
            else:
                help[place] = 0
        i += 1
    return ans


def checkGreedy():
    print("Check Greedy algorithms:")
    listTwoStr = [["abcbdab", "bdcaba"],
                  ["abcd", "acd"],
                  ["cdbac", "abdbb"],
                  ["abcabdc", "abcbdcbad"],
                  ["abcabdc", "xyz"],
                  ["acccccccb", "bccccccca"]]

    for i in range(len(listTwoStr)):
        print(f"LCS({listTwoStr[i][0]},{listTwoStr[i][1]}) is ", greedy(listTwoStr[i][0], listTwoStr[i][1]))


def checkGreedyWithHelp():
    print("Check GreedyWithHelpArray algorithms:")
    listTwoStr = [["abcbdab", "bdcaba"],
                  ["abcd", "acd"],
                  ["cdbac", "abdbb"],
                  ["abcabdc", "abcbdcbad"],
                  ["abcabdc", "xyz"],
                  ["acccccccb", "bccccccca"]]

    for i in listTwoStr:
        print(f"LCS({i[0]},{i[1]}) is", greedyWithHelp(i[0], i[1]))


###########################################
checkGreedy()
checkGreedyWithHelp()


