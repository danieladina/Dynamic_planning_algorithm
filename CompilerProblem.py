import random


class Program:
    '''
    * This class represents a program with 3 attributes:
    * a name of the program, a length of the program and a frequency of the program call
    '''
    name, len, freq = "", 0, 0

    def __init__(self, name, len, freq):
        self.name = name
        self.len = len
        self.freq = freq

    def __str__(self):
        return "[" + str(self.name) + "," + str(self.len) + "," + str(self.freq) + "]"


class CompilerProblem:
    def __init__(self, num_programs=10):
        self._numProg = num_programs
        self._setListPrograms = [Program("f" + str(i + 1), int(random.random() * 10000), int(random.random() * 100))
                                 for i in range(self._numProg)]
        print("The list of programs:")
        for pr in self._setListPrograms:
            print(pr)

    def getOptimalOrder(self):
        '''
        Creating an optimal order of the programs and calculation of a total time
        :return: print the optimal order of the programs and the total time
        '''
        programs = self._setListPrograms
        size_list = self._numProg
        self.mergeSort(programs, 0, size_list)
        totalTime, totallen = 0, 0
        print("The optimal order of programs:")
        for i in range(size_list):
            print(programs[i])
            totalTime += (totallen + programs[i].len) * programs[i].freq
            totallen += programs[i].len
        print("Total time:", totalTime)

    def mergeSort(self, p, low, high):
        n = high - low
        if n <= 1:
            return
        mid = (low + high) // 2
        self.mergeSort(p, low, mid)
        self.mergeSort(p, mid, high)
        i, j, k = low, mid, 0
        temp = []
        while i < mid and j < high:
            t1 = float(p[i].freq / p[i].len)
            t2 = float(p[j].freq / p[j].len)
            if t1 < t2:
                temp.insert(k, p[i])  # temp[k] = p[i]
                k += 1
                i += 1
            else:
                temp.insert(k, p[j])  # temp[k] = p[j]
                k += 1
                j += 1
        while i < mid:
            temp.insert(k, p[i])  # temp[k] = p[i]
            k += 1
            i += 1
        while j < high:
            temp.insert(k, p[j])  # temp[k] = p[j]
            k += 1
            j += 1
        for l in range(n):
            p[low + l] = temp[l]


if __name__ == '__main__':
    cp = CompilerProblem()
    cp.getOptimalOrder()
