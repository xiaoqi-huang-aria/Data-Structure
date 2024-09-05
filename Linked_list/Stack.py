from SingleLL import SingleLinkedList

class Stack:

    def __init__(self):
        """Create an empty stack consisting of an empty linkedlist."""
        self._inside = SingleLinkedList()

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._inside)

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._inside.is_empty()
    
    def peek(self):
        """Return (but do not remove) the element at the top of the stack.
           Return None if the stack is empty.
        """
        return self._inside.top()

    def push(self, e):
        """Add element e to the top of the stack."""
        self._inside.insert_from_head(e)

    def pop(self):
        """Remove and return the element from the top of the stack.
           Return None if the stack is empty.
        """
        return self._inside.delete_from_head()

    def __str__(self):
        return str(self._inside)

