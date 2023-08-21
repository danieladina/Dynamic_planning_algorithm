import random
# This code represents an implementation of the parking problem by the Doubly Circular Linked List.
class Node:
    # Attributes of the class
    __data = ''
    __next = None
    __prev = None

    # Constructor
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    # Methods:
    def __str__(self):
        return "" + self.__data

    def setData(self, value):
        self.__data = value

    def getData(self):
        return self.__data

    def setNext(self, next):
        self.__next = next

    def getNext(self):
        return self.__next

    def setPrev(self, prev):
        self.__prev = prev

    def getPrev(self):
        return self.__prev


class DoubleCycleLinkedList:
    # Constructor - constructs an empty list
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # Methods:
    # Insert element at the end of this list
    def add(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            self.__tail = self.__head
            self.__head.setNext(self.__tail)
            self.__head.setPrev(self.__tail)
        else:
            new_node.setNext(self.__head)
            new_node.setPrev(self.__tail)
            self.__tail.setNext(new_node)
            self.__tail = new_node
            self.__head.setPrev(self.__tail)
        self.__size += 1

    def getHead(self):
        return self.__head

    def __str__(self):
        s = "["
        if self.__head is not None:
            temp = self.__head
            while temp is not None and temp is not self.__tail:
                s += temp.getData() + ", "
                temp = temp.getNext()
        if temp is None:
            return s + "]"
        return s + self.__tail.getData() + "]"


class CalcCarsLinkList:
    def __init__(self, sizeMax=13):
        self._cars = DoubleCycleLinkedList()
        for i in range(sizeMax):
            c = chr(random.randint(65, 90))
            #while c == "V" or c == "W":
                #c = chr(random.randint(65, 90))
            self._cars.add(c)
        print(self._cars)

    def calcCars(self):
        '''
        Cars calculation: parking problem with double cycle linked list
        Complexity: O(n^2)
        :return: number of cars
        '''
        copyListCars = self._cars
        if copyListCars.getHead() is None:
            return 0
        temp = copyListCars.getHead()
        copyListCars.getHead().setData("V")
        temp = temp.getNext()
        count = 1
        while True:
            if temp.getData() == "V":
                temp.setData("W")
                steps = count
                while steps > 0:
                    temp = temp.getPrev()
                    steps -= 1
                if temp.getData() == "W":
                    break
                else:
                    count = 1
                    temp = copyListCars.getHead()
                    temp = temp.getNext()
            else:
                temp = temp.getNext()
                count += 1

        return count

    def calcCarsTwoPointers(self):
        '''
        Cars calculation: parking problem with two pointers
        Complexity: O(n)
        :return: number of cars
        '''
        if self._cars.getHead() is None:
            return 0
        headNode = self._cars.getHead()
        nodeForward = headNode.getNext()
        count = 1
        while nodeForward is not headNode:
            nodeForward = nodeForward.getNext()
            count += 1
        return count

if __name__ == '__main__':
    '''
    Capital letters are in range of 65, 90
    small letters are in the range 97 (ascii 'a' is 97,), 97+26-1 (there are 26 letters in the alphabet)
    arr = [chr(random.randrange(65,90)) for i in range(13)]
    print("array:", arr)

    print(chr(90))
    '''

    parking = CalcCarsLinkList()
    print("number of cars by DCLL =", parking.calcCars())
    print("number of cars by two pointers =", parking.calcCarsTwoPointers())
