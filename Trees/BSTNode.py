class BSTNode:

    def __init__(self, new_value):
        self.value = new_value
        self.counter = 1
        self._left = None
        self._right = None
        self._parent = None


    """ Returns True if this node is a leaf, False otherwise
    """
    def is_leaf(self):
        if self._left is None and self._right is None:
            return True
        else:
            return False


    """ Returns the number of children this node has
        0 => node is a leaf
        1 => node has a unique child (right or left)
        2 => node has two children (right and left)
    """
    def nb_of_children(self):
        result = 0
        if self._left is not None:
            result += 1
        if self._right is not None:
            result += 1
        return result


    """ Returns the height of the subtree of this node (min. is 1)
    """
    def height(self):
        height = 1
        if not self.is_leaf():
            if self._left is not None:
                height += self._left.height()
            if self._right is not None:
                height = max(height, 1 + self._right.height())
        return height


    """ Inserts value v in this node's subtree
        If v is already present, increment the counter on the container node
        Otherwise, add a new node containing value v
        Returns a reference to the newly added node
    """
    def add(self, v):
        added_node = None
        if v == self.value:
            self.counter += 1
            return self
        elif v < self.value:
            if self._left is None:
                added_node = BSTNode(v)
                added_node._parent = self
                self._left = added_node
            else:
                added_node = self._left.add(v)
        else:
            if self._right is None:
                added_node = BSTNode(v)
                added_node._parent = self
                self._right = added_node
            else:
                added_node = self._right.add(v)
        return added_node



    """ Returns a reference to the node that contains value v
        Returns None if v is not present in the tree
    """
    def find(self, v):
        if v == self.value:
            return self
        elif v < self.value and self._left is not None:
            return self._left.find(v)
        elif v > self.value and self._right is not None:
            return self._right.find(v)
        else:
            return None


    """ Returns a sorted list of all the values contained in this node's subtree
        ***Duplicates included***
    """
    def list_in_order(self):
        #TODO
        left = self._left.list_in_order() if self._left else []
        this = [self.value] * self.counter
        right = self._right.list_in_order() if self._right else []
        return left + this + right


    """ Removes this node from the tree
        Returns a reference to the node that remains
        #   None if removed node is a leaf
        #   child if removed node has only one child
        #   itself if removed node has two children =>
        #        ***removes its successor instead***
    """
    def remove(self):
        if self.is_leaf():
            if self._parent:
                if self._parent._left == self:
                    self._parent._left = None
                else:
                    self._parent._right = None
            return None
        elif self.nb_of_children() == 1:
            child = self._left if self._left else self._right
            if self._parent:
                if self._parent._left == self:
                    self._parent._left = child
                else:
                    self._parent._right = child
            child._parent = self._parent
            return child
        else:  
            successor = self._right
            while successor._left:
                successor = successor._left
            self.value = successor.value
            self.counter = successor.counter
            return successor.remove()