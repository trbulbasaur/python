class Node:
    def __init__(self, data):
        self._data = data
        self._nextNode = None

    @property
    def data(self):
        return self._data

    @property
    def nextNode(self):
        return self._nextNode

    @nextNode.setter
    def nextNode(self, value):
        self._nextNode = value


class LinkedList:
    def __init__(self):
        self._rootNode = None

    def add(self, data):
        tmp = Node(data)
        if self._rootNode == None:
            self._rootNode = tmp
            return
        v = self._rootNode
        while v.nextNode != None:
            v = v.nextNode

        v.nextNode = tmp

    def dump(self):
        if self._rootNode == None:
            return
        v = self._rootNode
        while v != None:
            print(v.data)
            v = v.nextNode

    def delete(self, data):
        if self._rootNode == None:
            return
        if self._rootNode.data == data:
            self._rootNode = self._rootNode.nextNode
            return
        v1 = self._rootNode
        v2 = v1.nextNode
        while v2 != None:
            if v2.data == data:
                v1.nextNode = v2.nextNode
                return
            v1 = v2
            v2 = v2.nextNode

    def findCycle(self):
        if self._rootNode == None:
            print("LinkedList Boştur..")
            return
        if self._rootNode.nextNode == None:
            print("LinkedList Tek Elemanlıdır..")
            return
        if self._rootNode.nextNode == self._rootNode:
            print("LinkedList İlk Node'dan cycledadır..")
            print("Node'un değeri : ", self._rootNode.data)
            return
        slowptr = self._rootNode
        fastptr = slowptr.nextNode.nextNode
        cycle = False
        while fastptr != None:
            slowptr = slowptr
            fastptr = fastptr.nextNode
            if fastptr == slowptr:
                cycle = True
                print("Cycle Vardır.")
                print("Cycle başladığı node'un değeri : ", slowptr.data)
                break
            slowptr = slowptr.nextNode
            fastptr = fastptr.nextNode
        if cycle == False:
            print("Cycle yoktur.")
            return

    def doCycle(self):
        rtnode = self._rootNode
        rtnode.nextNode.nextNode.nextNode.nextNode.nextNode=rtnode.nextNode


if __name__ == "__main__":
    a = LinkedList()
    a.add(6)
    a.add(7)
    a.add(8)
    a.add(9)
    a.add(10)
    print("--" * 10)
    a.doCycle()
    a.findCycle()
    print("--" * 10)