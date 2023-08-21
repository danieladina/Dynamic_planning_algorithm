'''
* Game Numbers - dynamic algorithm
* Complexity: O(n^2)
'''

def buildMatrix(arr):
    '''
    Creating a matrix of profits
    :param arr: Series of numbers
    :return: matrix of profits
    '''
    n = len(arr)
    # mat = [[0 for x in range(n)] for x in range(n)]
    mat = [[0] * n for x in range(n)]
    for i in range(n):
        mat[i][i] = arr[i]
    i = n - 2
    while i >= 0:
        for j in range(i+1, n):
            mat[i][j] = max(int(arr[i]) - int(mat[i + 1][j]), int(arr[j]) - int(mat[i][j - 1]))
        i -= 1
    # print(mat)
    return mat

def getDifference():
    return mattrix[0][len(mattrix[0])-1]

def getOptimalPathRec():
    return getOptimalPath(0, len(mattrix[0])-1)

def getOptimalPath(i, j):
    if i == j:
        return "("+str(i)+")" + str(mattrix[i][i])
    if mattrix[i][i] - mattrix[i+1][j] > mattrix[j][j] - mattrix[i][j-1]:
        return "(" + str(i) + ")" + str(mattrix[i][i]) + "->" + getOptimalPath(i + 1, j)
    else:
        return "(" + str(j) + ")" + str(mattrix[j][j]) + "->" + getOptimalPath(i, j - 1)

def gameStrategy(game):
    n = len(game)
    begin, end = 0, n - 1
    first, second, firstSum, secondSum = 0, 0, 0, 0
    step = 1
    mat = buildMatrix(game)
    print("*********** THIS IS A GAME **********")
    print(game)
    while end > begin:
        print("******* step #", step, "*******")
        # the first player ( Alice ) takes a number:
        print(game[begin:end + 1])
        if game[begin]-mat[begin + 1][end] > game[end] - mat[begin][end - 1]:
            print("ALICE: I take the first:", game[begin])
            firstSum += game[begin]
            first = begin
            begin += 1
        else:
            print("ALICE: I take the last:", game[end])
            firstSum += game[end]
            first = end
            end -= 1
        # the second player ( Bob ) takes a number:
        print(game[begin:end + 1])
        if game[begin]- mat[begin + 1][end] > game[end] - mat[begin][end - 1]:
            print("BOB: I take the first:", game[begin])
            secondSum = secondSum + game[begin]
            second = begin
            begin += 1
        else:
            print("BOB: I take the last:", game[end])
            secondSum = secondSum + game[end]
            second = end
            end -= 1
        step += 1
        print("Sum - ALICE:", firstSum, ", BOB:", secondSum)
    if len(game)%2!=0: # the first takes the last element
        print("******* step #", step, "*******")
        print("ALICE: I take the last:", game[end])
        firstSum += game[end]
        first = end
        print("Sum - ALICE:", firstSum, ", BOB:", secondSum)
    print("Congratulations! Sum of first player (Alice) =", firstSum, ", Sum of second player (BOB) =", secondSum, ", diff =", int(firstSum - secondSum))



# Sum of first player (Alice) = 23 , Sum of second player (BOB) = 23 , diff = 0
# array = [ 6, 9, 1, 2, 16, 12]

# Sum of first player (Alice) = 21 , Sum of second player (BOB) = 15 , diff = 6
# array = [5, 20, 10, 1]

# Sum of first player (Alice) = 12 , Sum of second player (BOB) = 9 , diff = 3
# array = [3, 4, 6, 2, 1, 5]

# Sum of first player (Alice) = 4 , Sum of second player (BOB) = 8 , diff = -4
# array = [3, 8, 1]

# Sum of first player (Alice) = 13 , Sum of second player (BOB) = 7 , diff = 6
array = [1, 3, 6, 1, 3, 6]



gameStrategy(array)


mattrix = buildMatrix(array)
print("\nDifference:", getDifference())
print("OptimalPath:", getOptimalPathRec())