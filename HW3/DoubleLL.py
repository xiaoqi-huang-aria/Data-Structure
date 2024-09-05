from queue import Empty


class DoubleLinkedList:
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_next', '_prev'  # streamline memory usage

        def __init__(self, element, prev, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._prev = prev  # reference to prev node
            self._next = next  # reference to next node

    def __init__(self):
        """Create an empty linkedlist."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the list.
        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._head._element  # front aligned with head of list

    def last(self):
        """Return (but do not remove) the element at the end of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._tail._element

    def delete_first(self):
        """Remove and return the first element of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():  # special case as deque is empty
            self._tail = None  # removed head had been the tail
        else:
            self._head._prev = None
        return answer

    def delete_last(self):
        """Remove and return the last element of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        answer = self._tail._element
        self._tail = self._tail._prev
        self._size -= 1
        if self.is_empty():  # special case as deque is empty
            self._head = None  # removed tail had been the head
        else:
            self._tail._next = None
        return answer

    def add_first(self, e):
        """Add an element to the front of list."""
        newest = self._Node(e, None, self._head)  # node will be new head node, next point to old head
        if self.is_empty():
            self._tail = newest  # special case: previously empty
        else:
            self._head._prev = newest
        self._head = newest
        self._size += 1

    def add_last(self, e):
        """Add an element to the back of list."""
        newest = self._Node(e, self._tail, None)  # node will be new tail node, prev point to old tail
        if self.is_empty():
            self._head = newest  # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest  # update reference to tail node
        self._size += 1

    def __str__(self):
        result = []
        curNode = self._head
        while (curNode is not None):
            result.append(str(curNode._element) + " <--> ")
            curNode = curNode._next
        result.append("None")
        return "".join(result)

    def remove_intersection(self, otherlist):
        """
        @otherlist: class DoubleLinkedList. Use values stored within this list.

        In this linked list, remove every node that contains a value appearing in otherlist.

        Example:
        self list(l1):
        18 <--> 16 <--> 14 <--> 12 <--> 10 <--> 18 <--> 16 <--> 14 <--> 12 <--> 10 <--> None
        otherlist:
        18 <--> 16 <--> 14 <--> 12 <--> None
        >>> l1.del_anything_occured(otherlist)
        l1 should become:
            10 <--> 10 <--> None
        otherlist should remain the same:
            18 <--> 16 <--> 14 <--> 12 <--> None
        """
        # TODO: Problem 4
        # Create a set of elements from otherlist for quick lookup
        elements = set()
        cur = otherlist._head
        while cur is not None:
            elements.add(cur._element)
            cur = cur._next

        # Traverse the current list and remove nodes with elements in other_elements
        cur = self._head
        while cur is not None:
            next_node = cur._next
            if cur._element in elements:
                if cur._prev is not None:
                    cur._prev._next = cur._next
                else:
                    self._head = cur._next
                if cur._next is not None:
                    cur._next._prev = cur._prev
                else:
                    self._tail = cur._prev
                self._size -= 1
            cur = next_node

def main():
    print("-----------Testing del_anything_occured-------------")
    l1 = DoubleLinkedList()
    l2 = DoubleLinkedList()
    for i in range(10):
        l1.add_first(i * 2)
    for j in range(10):
        l2.add_first(j * 3)
    print(l1)  # 18 <--> 16 <--> 14 <--> 12 <--> 10 <--> 8 <--> 6 <--> 4 <--> 2 <--> 0 <--> None
    print(l2)  # 27 <--> 24 <--> 21 <--> 18 <--> 15 <--> 12 <--> 9 <--> 6 <--> 3 <--> 0 <--> None
    l1.remove_intersection(l2)
    print(l1, ", Expected: 16 <--> 14 <--> 10 <--> 8 <--> 4 <--> 2 <--> None")
    print(l2, ", l2 should remain the same.")


if __name__ == "__main__":
    main()
