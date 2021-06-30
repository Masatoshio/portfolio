# creating a singly linked list class
class LList:

    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None

    def addFront(self, val):
        self.head = self.Node(val, self.head)

    def getFront(self):
        if self.head is None:
            return None
        else:
            return self.head.val

    def removeFront(self):
        if self.head is not None:
            self.head = self.head.next

    def addBack(self, val):
        if self.head is None:
            self.addFront(val)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = self.Node(val)


# creating a doubly linked list class
class DLList:

    class Node:
        def __init__(self, val, prev, next):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, lst=[]):
        self.head = None
        self.tail = None
        self.size = 0
        for x in lst:
            self.addBack(x)

    def addBack(self, val):
        newNode = self.Node(val, self.tail, None)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def addFront(self, val):
        newNode = self.Node(val, None, self.head)
        if self.head is None:
            self.tail = newNode
        else:
            self.head.prev = newNode
        self.head = newNode
        self.size += 1

    def peekFront(self):
        return self.head.val

    def peekBack(self):
        return self.tail.val

    def count(self):
        return self.size

    def deleteNode(self, n):
        if n.prev is not None:
            n.prev.next = n.next
        if n.next is not None:
            n.next.prev = n.prev
        if n is self.head:
            self.head = n.next
        if n is self.tail:
            self.tail = n.prev

        self.size -= 1

    def removeFront(self):
        self.deleteNode(self.head)

    def removeBack(self):
        self.deleteNode(self.tail)

    def findNode(self, ind):
        if ind < 0 or ind >= len(self):
            raise IndexError
        if ind < len(self // 2):
            n = self.head
            for i in range(ind):
                n = n.next
            return n
        else:
            n = self.tail
            for n in range(len(self) - ind - 1):
                n = n.prev
            return n

    def __getitem__(self, ind):
        return self.findNode(ind.val)

    def delete(self, ind):
        self._deleteNode(self._findNode(ind))

    def __iter__(self):
        n = self.head
        while n is not None:
            yield n.val
            n = n.next

    def __reversed__(self):
        print("reverse")
        n = self.tail
        while n is not None:
            yield n.val
            n = n.prev
