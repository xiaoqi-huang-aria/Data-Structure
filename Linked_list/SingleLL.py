#### Original author: Ratan Kumar Dey @ NYU Shanghai ####

class SingleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
            self._element = element               # reference to user's element
            self._next = next                     # reference to next node

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
           Print if the linkedlist is empty and return None.
        """
        if self.is_empty():
            return None
        return self._head._element

    def insert_from_head(self, e):
        """Add element e to the head of the linkedlist."""
        new_node = self._Node(e,self._head)
        self._head = new_node
        self._size += 1

    def delete_from_head(self):
        """Remove and return the element from the head of the linkedlist.
           Print if the linkedlist is empty and return None.
        """
        if self.is_empty():
            return None
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

    def return_max(self):  
        """Find and return the largest element in the linkedlist.
           Print if the linkedlist is empty and return None.
        """
        if self.is_empty():
            print("The linked list is empty")
            return None
        max_element = self._head._element
        cur = self._head._next
        while cur is not None:
            if cur._element > max_element:
                max_element = cur._element
            cur = cur._next
        return max_element

    def insert_after_kth_index(self, k, e):
        """Insert an element after the kth index in the list.
            Print if the linkedlist is smaller than k.
        """
        if k >= self._size:
            print(f"The linked list is smaller than index {k}")
            return None
        cur = self._head
        for _ in range(k):
            cur = cur._next
        new_node = self._Node(e, cur._next)
        cur._next = new_node
        self._size += 1


