class Node:
    '''
    * class Node:
    * x,y - the price for get down (y) or left (x)
    * price - the best price from (0,0) to this node
    * price2 - the second best price from (0,0) to this node
    * priceFromTheEnd - the best price from (m,n) to this node
    * numOfPaths - number of shortest paths until this node
    '''
    x, y, price, numOfPaths = 0, 0, 0, 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.price = 0
        self.numOfPaths = 0
        self.priceFromTheEnd = 0
        self.price2 = 0

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ") "
        # return "x=" + str(self.x) + ", y=" + str(self.y) + ", price=" + str(price) + ", numPath=" + str(numOfPaths) + "; "


class AeroplaneProblem:
    '''
    /**
    * class AeroplaneProblem presents
    * how find one best/cheapest path, all best/cheapest paths
    * and more creative questions
    */
    '''
    numOfPaths, cheapestPrice = 0, 0
    mat = []

    def __init__(self, nodes):
        self.numOfPaths = 0
        self.cheapestPrice = 0
        self.mat = nodes

    def getBestPrice(self):
        '''
        * Build a matrix that contains the price to get each point (from (0,0))
        * and the number of shortest path until each point
        * Complexity: O(n*m)
        :return:
        '''
        # n rows, m columns
        n = len(self.mat)
        m = len(self.mat[0])
        self.mat[0][0].price = 0
        # first column:
        for i in range(1, n):
            self.mat[i][0].price = int(self.mat[i - 1][0].y) + int(self.mat[i - 1][0].price)
            self.mat[i][0].numOfPaths = 1
        # first row:
        for j in range(1, m):
            self.mat[0][j].price = int(self.mat[0][j - 1].price) + int(self.mat[0][j - 1].x)
            self.mat[0][j].numOfPaths = 1
        for i in range(1, n):
            for j in range(1, m):
                a = int(self.mat[i - 1][j].price) + int(self.mat[i - 1][j].y)
                b = int(self.mat[i][j - 1].price) + int(self.mat[i][j - 1].x)
                if a < b:
                    self.mat[i][j].price = a
                    self.mat[i][j].numOfPaths = self.mat[i - 1][j].numOfPaths
                elif a > b:
                    self.mat[i][j].price = b
                    self.mat[i][j].numOfPaths = self.mat[i][j - 1].numOfPaths
                else:  # x==y
                    self.mat[i][j].price = a
                    self.mat[i][j].numOfPaths = int(self.mat[i][j - 1].numOfPaths) + int(self.mat[i - 1][j].numOfPaths)

        self.numOfPaths = self.mat[n - 1][m - 1].numOfPaths
        self.cheapestPrice = self.mat[n - 1][m - 1].price

    def getNumOfPaths(self):
        return self.numOfPaths

    def getCheapestPrice(self):
        return self.cheapestPrice

    def printNodes(self):
        '''
        Print matrix of nodes
        :return:
        '''
        print("Matrix of nodes:")
        n = len(self.mat)
        m = len(self.mat[0])
        for i in range(n):
            for j in range(m):
                print(self.mat[i][j], end="")
            print()

    def printPrices(self):
        '''
        Print matrix of prices
        :return:
        '''
        print("Matrix of prices:")
        n = len(self.mat)
        m = len(self.mat[0])
        for i in range(n):
            for j in range(m):
                print(self.mat[i][j].price, "\t", end="")
            print()

    def getOneCheapestPath(self):
        '''
        Calculate One Best Path by Induction
        Complexity: O(n+m) - but first need to build the matrix - O(n*m)
        :return: one of shortest path - induction
        '''
        ans = ""
        i = len(self.mat) - 1
        j = len(self.mat[0]) - 1
        while i > 0 and j > 0:
            a = int(self.mat[i - 1][j].price) + int(self.mat[i - 1][j].y)
            b = int(self.mat[i][j - 1].price) + int(self.mat[i][j - 1].x)
            if a < b:
                ans = "1" + ans
                i -= 1
            else:
                ans = "0" + ans
                j -= 1
        if i == 0:
            while j > 0:
                ans = "0" + ans
                j -= 1
        else:  # j==0
            while i > 0:
                ans = "1" + ans
                i -= 1
        return ans

    def AllPathsRecurs(self, teta):
        paths = []
        self.buildPaths("", len(self.mat)-1, len(self.mat[0])-1, paths)
        print(paths)

    def buildPaths(self, path, i, j, paths):
        if i == 0 and j == 0:
            paths.append(path)
        elif i == 0 and j > 0:
            '''
            t = ""
            for k in range(j):
                t = t + "0"
            paths.add(t + path)
            '''
            self.buildPaths("0" + path, i, j - 1, paths)
        elif j == 0 and i > 0:
            '''
            t = ""
            for k in range(i):
                t = t + "1"
            paths.add(t + path)
            '''
            self.buildPaths("1" + path, i - 1, j, paths)
        else:
            a = self.mat[i - 1][j].price + self.mat[i - 1][j].y
            b = self.mat[i][j - 1].price + self.mat[i][j - 1].x
            if a < b:
                self.buildPaths("1" + path, i - 1, j, paths)
            elif a > b:
                self.buildPaths("0" + path, i, j - 1, paths)
            else:  # a==b
                self.buildPaths("1" + path, i - 1, j, paths)
                self.buildPaths("0" + path, i, j - 1, paths)


import InitMatrixOfPrices

if __name__ == '__main__':
    nodes = InitMatrixOfPrices.initMatOfNodes1()
    ap = AeroplaneProblem(nodes)
    ap.printNodes()
    ap.getBestPrice()
    ap.printPrices()
    print("The price of the cheapest path:", ap.getCheapestPrice())
    print("The number of the cheapest paths:", ap.getNumOfPaths())
    print("One cheapest path:", ap.getOneCheapestPath())
    teta = 10
    print("\nAll cheapest paths: ")
    ap.AllPathsRecurs(teta)
