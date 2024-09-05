from BSTNode import BSTNode

class BinarySearchTree:

    def __init__(self):
        self._root = None

    """ Returns True if this tree is empty, False otherwise
    """
    def is_empty(self):
        return (self._root == None)

    """ Returns the node at the root of this tree, None if it's empty
    """
    def get_root(self):
        return self._root


    """ Returns the height of the tree, 0 if it's empty
    """
    def height(self):
        if self.is_empty():
            return 0
        return self._root.height()
        
    """ Inserts value v in this tree
        Returns a reference to the node that contains v
    """
    def add(self, v):
        if self.is_empty():
            self._root = BSTNode(v)
            return self._root
        else:
            return self._root.add(v)

    """ Returns a reference to the node that contains v
        None if the tree doesn't contain v
    """
    def find(self, v):
        if self.is_empty():
            return None
        return self._root.find(v)

    """ Returns the sorted list of all values in this tree
        *** [] if it's empty ***
        *** Duplicates included ***
    """
    def list_in_order(self):
        if self.is_empty():
            return []
        return self._root.list_in_order()

    """ Returns the level-ordered list of all values in this tree
        *** [] if it's empty ***
        *** Duplicates included ***
    """
    def list_breadth_first(self):
        if self.is_empty():
            return []
        result = []
        queue = [self._root]
        while queue:
            node = queue.pop(0)
            result.extend([node.value] * node.counter)
            if node._left:
                queue.append(node._left)
            if node._right:
                queue.append(node._right)

        return result

    """ Removes value v from the tree
        #Skip node removal if
        #       (a) value doesn't occur in the tree
        #       (b) counter is higher than 1 (decrement counter)
        Returns a reference to the node containing v
    """
    def remove(self, v):
        #TODO
        node_to_remove = self.find(v)
        if node_to_remove is None:
            return None
        if node_to_remove.counter > 1:
            node_to_remove.counter -= 1
            return node_to_remove
        r = node_to_remove.remove()
        if node_to_remove == self._root:
            self._root = r
            if r is not None:
                r._parent = None
            return node_to_remove