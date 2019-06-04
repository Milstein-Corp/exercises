# Definition for singly-linked list.
from collections import defaultdict


def printl(l, header):
    cur = l
    print(header, end=": ")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.pre = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.size <= index or index < 0:
            return -1
        else:
            n = 0
            cur = self.head
            while n != index:
                n += 1
                cur = cur.next

        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        n = Node(val)
        n.next = self.head
        self.head = n
        if self.size == 0:
            self.tail = self.head

        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.size == 0:
            self.head = Node(val)
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next = Node(val)
            self.size += 1
            self.tail = self.tail.next

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            index = 0
        if not 0 <= index <= self.size:
            return None

        if self.size == 0:
            new = Node(val)
            self.head = new
            self.tail = new
            self.size += 1
            return

        if index == 0:
            new = Node(val)
            new.next = self.head
            self.head = new
            self.size += 1
            return
        n = 0
        cur = self.head
        while n != index - 1:
            cur = cur.next
            n += 1

        new = Node(val)
        new.next = cur.next
        cur.next = new
        if index == self.size:
            self.tail = self.tail.next
        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if not 0 <= index < self.size:
            return None

        if self.size == 1:
            self.size -= 1
            self.head = None
            self.tail = None
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        n = 0
        cur = self.head
        while n < index - 1:
            n += 1
            cur = cur.next

        if index == self.size-1:
            self.tail = cur
        cur.next = cur.next.next
        self.size -= 1


if __name__ == '__main__':
    # initialize
    print("INITIALIZE")
    obj = MyLinkedList()
    print("type: %s " % type(obj))
    print("head: %s " % obj.head)
    print("tail: %s " % obj.tail)
    print()

    # add
    print("ADD at HEAD")
    print("add a zero")
    obj.addAtHead(0)
    print("value of head    : %s " % obj.head.val)
    print("value of tail    : %s " % obj.tail.val)
    print("value at index 0 : %s " % obj.get(0))
    print("value at index 1 : %s " % obj.get(1))
    print("value at index 2 : %s " % obj.get(2))
    print("value at index -1: %s " % obj.get(-1))
    print("add a 22")
    print(obj.addAtHead(22))
    print("value of head    : %s " % obj.head.val)
    print("value of tail    : %s " % obj.tail.val)
    print("value at index 0 : %s " % obj.get(0))
    print("value at index 1 : %s " % obj.get(1))
    print("value at index 2 : %s " % obj.get(2))
    print("value at index -1: %s " % obj.get(-1))

    # add at tail
    print("ADD AT TAIL")
    obj = MyLinkedList()
    print("add a zero")
    obj.addAtTail(0)
    print("value of head    : %s " % obj.head.val)
    print("value of tail    : %s " % obj.tail.val)
    print("value at index 0 : %s " % obj.get(0))
    print("value at index 1 : %s " % obj.get(1))
    print("value at index 2 : %s " % obj.get(2))
    print("value at index -1: %s " % obj.get(-1))
    print("add a 22")
    print(obj.addAtTail(22))
    print("value of head    : %s " % obj.head.val)
    print("value of tail    : %s " % obj.tail.val)
    print("value at index 0 : %s " % obj.get(0))
    print("value at index 1 : %s " % obj.get(1))
    print("value at index 2 : %s " % obj.get(2))
    print("value at index -1: %s " % obj.get(-1))

    # add at index
    print("ADD AT INDEX")
    obj = MyLinkedList()
    print("add a zero and a 22")
    obj.addAtTail(0)
    obj.addAtTail(22)
    print("value of head    : %s " % obj.head.val)
    print("value of tail    : %s " % obj.tail.val)
    print("value at index 0 : %s " % obj.get(0))
    print("value at index 1 : %s " % obj.get(1))
    print("value at index 2 : %s " % obj.get(2))
    print("value at index -1: %s " % obj.get(-1))
    print("add a 55 at the 1 index")
    obj.addAtIndex(1, 55)
    print("value of head    : %s " % obj.head.val)
    print("value of tail    : %s " % obj.tail.val)
    print("value at index 0 : %s " % obj.get(0))
    print("value at index 1 : %s " % obj.get(1))
    print("value at index 2 : %s " % obj.get(2))
    print("value at index 3 : %s " % obj.get(3))
    print("value at index -1: %s " % obj.get(-1))

    # delete at index
    print("Delete AT INDEX")
    obj = MyLinkedList()
    print("add a zero and a 22 and a 44")
    obj.addAtTail(0)
    obj.addAtTail(22)
    obj.addAtTail(44)
    print("value of head    : %s " % obj.head.val)
    print("value of tail    : %s " % obj.tail.val)
    print("value at index 0 : %s " % obj.get(0))
    print("value at index 1 : %s " % obj.get(1))
    print("value at index 2 : %s " % obj.get(2))
    print("value at index -1: %s " % obj.get(-1))
    print("delete the thing a the 1 index")
    obj.deleteAtIndex(1)
    print("value of head    : %s " % obj.head.val)
    print("value of tail    : %s " % obj.tail.val)
    print("value at index 0 : %s " % obj.get(0))
    print("value at index 1 : %s " % obj.get(1))
    print("value at index 2 : %s " % obj.get(2))
    print("value at index 3 : %s " % obj.get(3))
    print("value at index -1: %s " % obj.get(-1))

    # delete at index
    print("Delete AT INDEX")
    obj = MyLinkedList()
    print("add a zero and a 22 and a 44")
    obj.addAtTail(0)
    obj.addAtTail(22)
    obj.addAtTail(44)
    print("value of head    : %s " % obj.head.val)
    print("value of tail    : %s " % obj.tail.val)
    print("value at index 0 : %s " % obj.get(0))
    print("value at index 1 : %s " % obj.get(1))
    print("value at index 2 : %s " % obj.get(2))
    print("value at index -1: %s " % obj.get(-1))
    print("delete the thing a the 0 index")
    obj.deleteAtIndex(0)
    print("value of head    : %s " % obj.head.val)
    print("value of tail    : %s " % obj.tail.val)
    print("value at index 0 : %s " % obj.get(0))
    print("value at index 1 : %s " % obj.get(1))
    print("value at index 2 : %s " % obj.get(2))
    print("value at index 3 : %s " % obj.get(3))
    print("value at index -1: %s " % obj.get(-1))

    # delete at index
    print("Delete AT INDEX")
    obj = MyLinkedList()
    print("add a zero and a 22 and a 44")
    obj.addAtTail(0)
    obj.addAtTail(22)
    obj.addAtTail(44)
    print("value of head    : %s " % obj.head.val)
    print("value of tail    : %s " % obj.tail.val)
    print("value at index 0 : %s " % obj.get(0))
    print("value at index 1 : %s " % obj.get(1))
    print("value at index 2 : %s " % obj.get(2))
    print("value at index -1: %s " % obj.get(-1))
    print("delete the thing a the 2 index")
    obj.deleteAtIndex(2)
    print("value of head    : %s " % obj.head.val)
    print("value of tail    : %s " % obj.tail.val)
    print("value at index 0 : %s " % obj.get(0))
    print("value at index 1 : %s " % obj.get(1))
    print("value at index 2 : %s " % obj.get(2))
    print("value at index 3 : %s " % obj.get(3))
    print("value at index -1: %s " % obj.get(-1))

    # obj.addAtTail(val)
    # obj.addAtIndex(index,val)
    # obj.deleteAtIndex(index)
