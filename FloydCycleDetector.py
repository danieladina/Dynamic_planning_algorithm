from random import *

# A Linked List Node
class Node:
    # Constructor
    def __init__(self, data = None, next=None):
        self.__data = data
        self.__next = next

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

# Definition for singly-linked list.
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def getHead(self):
        return self.__head

    def getSize(self):
        return self.__size

    # Insert element at the end of this list
    def insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            current = self.__head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(new_node)
        self.__size += 1

    def printLL(self):
        current = self.__head
        while current:
            print(current.getData())
            current = current.getNext()

    def __str__(self):
        s = "["
        if self.__head is not None:
            temp = self.__head
            while temp is not None:
                s += temp.getData()
                temp = temp.getNext()
                if temp is not None:
                    s +=  ", "
        return s + "]"

#  This class detects a cycle in a linked list using Floyd’s cycle detection algorithm
class FloydCycleDetector:
    # create a LinkedL ist
    def __init__(self, sizeMax=13):
        self._list = LinkedList()
        for i in range(sizeMax):
            l = chr(randint(65, 90))
            self._list.insert(l)
        print(self._list)

    # insert cycle from an ended node to a random node
    def createLoop(self):
        rand = self._list.getHead()
        last = self._list.getHead()
        while last.getNext() is not None:
            last = last.getNext()
        rand_index = randint(0,self._list.getSize())
        # print("rand_index=",rand_index)
        i = 0
        while i < rand_index and rand.getNext() is not None:
            rand = rand.getNext()
            i += 1
        last.setNext(rand)


    def hasLoop(self):
        '''
        Complexity: O(n)
        :return: true if the list has a loop otherwise, false
        '''
        head = self._list.getHead()
        if head is None or head.getNext() is None:
            return False
        slow = head
        fast = head
        while slow is not None and fast is not None and fast.getNext() is not None:
            slow = slow.getNext()
            fast = fast.getNext().getNext()
            if slow == fast:
                return True
        return False

    def findNodeMeeting(self):
        head = self._list.getHead()
        if head is None or head.getNext() is None:
            return head
        slow = head
        fast = head
        while slow is not None and fast is not None and fast.getNext() is not None:
            slow = slow.getNext()
            fast = fast.getNext().getNext()
            if slow == fast:
                break
        return fast

    def findNodeStartLoop(self, meetingNode):
        head = self._list.getHead()
        if head is None or head.getNext() is None:
            return head
        slow = head
        fast = meetingNode
        while slow is not fast:
            fast = fast.getNext()
            slow = slow.getNext()
            if slow == fast:
                break
        return slow

    def lengthLoop(self, startLoopNode):
        lenLoop = 0
        slow = startLoopNode
        fast = startLoopNode
        fast = fast.getNext()
        lenLoop += 1
        while slow is not fast:
            fast = fast.getNext()
            lenLoop += 1
        return lenLoop

if __name__ == '__main__':
    detect = FloydCycleDetector()
    print("Has the list a cycle?", detect.hasLoop())
    detect_ = FloydCycleDetector()
    detect_.createLoop()
    print("Has the list a cycle?", detect_.hasLoop())
    meetingNode = detect_.findNodeMeeting()
    print("Meeting node is", meetingNode)
    startLoopNode = detect_.findNodeStartLoop(meetingNode)
    print("Start loop node is", startLoopNode)
    lengthLoop = detect_.lengthLoop(startLoopNode)
    print("A length of the cycle is", lengthLoop)
