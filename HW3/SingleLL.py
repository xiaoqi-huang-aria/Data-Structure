from queue import Empty


class SingleLinkedList:
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

    def __init__(self):
        """Create an empty linkedlist."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the linkedlist."""
        return self._size

    def is_empty(self):
        """Return True if the linkedlist is empty."""
        return self._size == 0

    def top(self):
        """Return (but do not remove) the element at the top of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._head._element  # head of list

    def insert_from_head(self, e):
        """Add element e to the head of the linkedlist."""
        # Create a new link node and link it
        new_node = self._Node(e, self._head)
        self._head = new_node
        self._size += 1

    def delete_from_head(self):
        """Remove and return the element from the head of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        to_return = self._head._element
        self._head = self._head._next
        self._size -= 1
        return to_return

    def __str__(self):
        result = []
        curNode = self._head
        while (curNode is not None):
            result.append(str(curNode._element) + "-->")
            curNode = curNode._next
        result.append("None")
        return "".join(result)

    def remove_all_occurance(self, value):
        """
        @value: the value we are trying to remove from the self list.
        remove any node that contains value in self linked list. Return nothing.
        Example:
        l1: 5 --> 4 --> 2 --> 4 --> 1 --> 9 --> 4 --> None
        >>> l1.remove_all_occurance(4)
        l1 should become: 5 --> 2 --> 1 --> 9 --> None
        @return: Nothing
        """
        # TODO: Problem 1
        cur = self._head
        prev = None
        while cur is not None:
            if cur._element == value:
                if prev is None:
                    self._head = cur._next
                else:
                    prev._next = cur._next
                self._size -= 1
            else:
                prev = cur
            cur = cur._next

    def reverse(self):
        """
        reverses self list.
        Example:
        1 --> 2 --> 3 --> 4 --> None
        >>> l.reverse()
        4 --> 3 --> 2 --> 1 --> None
        @return: Nothing
        """
        # TODO: Problem 2
        cur = self._head
        prev = None
        while cur is not None:
            next_node = cur._next
            cur._next = prev
            prev = cur
            cur = next_node
        self._head = prev

    def sublist(self, otherlist):
        """
        @otherlist: class SingleLinkedList.
        Return True if otherlist is sublist of self. Return False otherwise.
        (Definition of sublist: A list that makes up part of a larger list)

        Example:
        self list(l1):
        1 --> 2 --> 3 --> 4 --> None
        otherlist:
        None; 1 --> None; 1 --> 2 --> None; 1 --> 2 --> 3 --> None;
        1 --> 2 --> 3 --> 4 --> None; 2 --> None; 2 --> 3 --> None;
        2 --> 3 --> 4 --> None; 3 --> None; 3 --> 4 --> None; 4 --> None
        Are valid sublists. Should return True for any of the above cases.
        >>> l1.sublist(otherlist)
        True

        otherlist:
        1 --> 1 --> None
        >>> l1.sublist(otherlist)
        False

        @return: True or False
        """
        # TODO: Problem 3
        if otherlist.is_empty():
            return True
        cur = self._head
        while cur is not None:
            if self.match(cur, otherlist._head):
                return True
            cur = cur._next
        return False

    def match(self, node1, node2):
        while node2 is not None:
            if node1 is None or node1._element != node2._element:
                return False
            node1 = node1._next
            node2 = node2._next
        return True
    
def main():
    print("-----------Testing remove_all_occurance-------------")
    l1 = SingleLinkedList()
    for i in range(10):
        l1.insert_from_head(6)
    print(l1)  # 6-->6-->6-->6-->6-->6-->6-->6-->6-->6-->None
    l1.remove_all_occurance(6)
    print(l1, "Expected: None")
    print()

    l1 = SingleLinkedList()
    for i in range(10):
        l1.insert_from_head(i % 2)
    print(l1)  # 1-->0-->1-->0-->1-->0-->1-->0-->1-->0-->None
    l1.remove_all_occurance(0)
    print(l1, "Expected: 1-->1-->1-->1-->1-->None")
    print()

    print("-----------Testing reverse-------------")
    l1 = SingleLinkedList()
    for i in range(10):
        l1.insert_from_head(i)
    print(l1)  # 9-->8-->7-->6-->5-->4-->3-->2-->1-->0-->None
    l1.reverse()
    print(l1, "Expected: 0-->1-->2-->3-->4-->5-->6-->7-->8-->9-->None")

    print("-----------Testing sublist-------------")
    l1 = SingleLinkedList()
    l2 = SingleLinkedList()
    for i in range(10):
        l1.insert_from_head(i)
    for i in range(5):
        l2.insert_from_head(i + 3)
    print(l1)
    print(l2)
    print("Is l2 sublist of l1? Your answer:", l1.sublist(l2), ", Expected: True")


if __name__ == "__main__":
    main()
