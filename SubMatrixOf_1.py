'''
Finding the largest square submatrix that consists the ones only
'''


def subMatrixOf1(mat):
    '''
    Dynamic algorithm:  for finding the biggest k*k matrix of '1'
    First Method: using one help matrix,
    where help[i,j] is the size of a square submatrix consisting of ones,
    whose lower right corner of the submatrix is the cell with coordinates [i,j].
    Complexity: O(m*n)
    :param mat: matrix filled with 0,1
    :return: print the size of a square submatrix consisting of ones and the coordinates of a cell in the lower right corner of this submatrix
    '''
    # h - help matrix:
    h = [[0 for i in range(0, len(mat[0]))] for j in range(0, len(mat))]
    max_dim, i_max, j_max = 0, 0, 0
    # copy first row from mat:
    for j in range(len(mat[0])):
        if mat[0][j] == 1:
            max_dim = 1
            i_max = 0
            j_max = j
        h[0][j] = mat[0][j]

    # copy first column from mat:
    for i in range(len(mat)):
        if mat[i][0] == 1:
            max_dim = 1
            i_max = 0
            j_max = i
        h[i][0] = mat[i][0]

    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            if mat[i][j] != 0:
                h[i][j] = min3(h[i - 1][j - 1], h[i - 1][j], h[i][j - 1]) + 1
                if h[i][j] > max_dim:
                    max_dim = h[i][j]
                    i_max = i
                    j_max = j

    print("Dynamic algorithm by using one help matrix:\nMatrix:")
    for row in mat:
        print(row)
    print("\nHelp Matrix:", )
    for row in h:
        print(row)
    print("max_dim:", max_dim, ", i_max:", i_max, ", j_max:", j_max)


def min3(a, b, c):
    min = a
    if min > b:
        min = b
    if min > c:
        min = c
    return min


def subMatrixOf1_3Matrices(mat):
    '''
    Dynamic algorithm:  for finding the biggest k*k matrix of '1'
    Second Method: using 3 help matrices:
    a first matrix represents the size of the ones sequence by rows,
    a second matrix represents the size of the ones sequence by columns,
    a third matrix represents the size of the ones square in each cell
    whose lower right corner of the submatrix is the cell with coordinates [i,j].
    Complexity: O(m*n)
    :param mat: matrix filled with 0,1
    :return: print the size of a square submatrix consisting of ones and the coordinates of a cell in the lower right corner of this submatrix
    '''
    rows, cols = len(mat), len(mat[0])
    max_dim, i_max, j_max = 0, 0, 0
    x = [[0 for i in range(cols)] for j in range(rows)]
    y = [[0 for i in range(cols)] for j in range(rows)]
    z = [[0 for i in range(cols)] for j in range(rows)]
    # fill first column of 3 matrix:
    for i in range(rows):
        x[i][0] = mat[i][0]
        y[i][0] = mat[i][0]
        z[i][0] = mat[i][0]
    # fill first row of 3 matrix:
    for j in range(cols):
        x[0][j] = mat[0][j]
        y[0][j] = mat[0][j]
        z[0][j] = mat[0][j]
    # fill 'rows' matrix:
    for i in range(1, rows):
        for j in range(1, cols):
            if mat[i][j] == 1:
                x[i][j] = x[i][j - 1] + 1
    # fill 'columns' matrix:
    for j in range(1, cols):
        for i in range(1, rows):
            if mat[i][j] == 1:
                y[i][j] = y[i - 1][j] + 1
    # fill 'answers' matrix:
    for i in range(1, rows):
        for j in range(1, cols):
            if mat[i][j] == 1:
                z[i][j] = min3(z[i - 1][j - 1] + 1, x[i][j], y[i][j])
                if z[i][j] > max_dim:
                    max_dim = z[i][j]
                    i_max = i
                    j_max = j
    print("Dynamic algorithm by using three help matrices:\nMatrix:")
    for row in mat:
        print(row)
    print("\nMatrix x:", )
    for row in x:
        print(row)
    print("\nMatrix y:", )
    for row in y:
        print(row)
    print("\nMatrix z:", )
    for row in z:
        print(row)
    print("max_dim:", max_dim, ", i_max:", i_max, ", j_max:", j_max)


###################################################################################
mat = [[1, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 0]]
subMatrixOf1(mat)
subMatrixOf1_3Matrices(mat)
mat1 = [[0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 1]]
subMatrixOf1(mat1)
subMatrixOf1_3Matrices(mat1)
mat2 = [[0, 0, 1, 0, 0], [1, 1, 1, 1, 0], [0, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 0, 0, 1]]
subMatrixOf1(mat2)
subMatrixOf1_3Matrices(mat2)
