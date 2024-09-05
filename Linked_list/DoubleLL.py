#### Original author: Ratan Kumar Dey @ NYU Shanghai ####

class DoubleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_next', '_prev'         # streamline memory usage

        def __init__(self, element, prev, next):      # initialize node's fields
            self._element = element               # reference to user's element
            self._prev = prev                     # reference to prev node
            self._next = next                     # reference to next node




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
           Print if the list is empty.
        """
        if self.is_empty():
            print("The linked list is empty")
            return None
        return self._head._element

    def last(self):
        """Return (but do not remove) the element at the end of the list.
           Print if the list is empty.
        """
        if self.is_empty():
            print("The linked list is empty")
            return None
        return self._tail._element


    def delete_first(self):
        """Remove and return the first element of the list.
           Print and return None if the list is empty.
        """
        if self.is_empty():
            print("The linked list is empty")
            return None
        to_return = self._head._element
        self._head = self._head._next
        if self._head is not None:
            self._head._prev = None
        else:
            self._tail = None
        self._size -= 1
        return to_return

    def delete_last(self):
        """Remove and return the last element of the list.
           Print and return None if the list is empty.
        """
        if self.is_empty():
            print("The linked list is empty")
            return None
        to_return = self._tail._element
        self._tail = self._tail._prev
        if self._tail is not None:
            self._tail._next = None
        else:
            self._head = None
        self._size -= 1
        return to_return


    def add_first(self, e):
        """Add an element to the front of list."""
        new_node = self._Node(e, None, self._head)
        if self.is_empty():
            self._tail = new_node
        else:
            self._head._prev = new_node
        self._head = new_node
        self._size += 1


    def add_last(self, e):
        """Add an element to the back of list."""
        new_node = self._Node(e, self._tail, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1



    def __str__(self):
        result = []
        curNode = self._head
        while (curNode is not None):
            result.append(str(curNode._element) + " <--> ")
            curNode = curNode._next
        result.append("None")
        return "".join(result)
