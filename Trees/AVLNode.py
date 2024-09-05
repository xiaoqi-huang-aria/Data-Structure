from BSTNode import BSTNode

class AVLNode (BSTNode):

    def __init__(self, new_value):
        self.value = new_value
        self.counter = 1
        self._left = None
        self._right = None
        self._parent = None

    def balance_factor(self):
        lheight, rheight = 0, 0
        if (self._left != None):
            lheight = self._left.height()
        if (self._right != None):
            rheight = self._right.height()
        return (lheight - rheight)

    def rotate_left(self):
        #Carry out rotation on pointers
        swap = self._right
        self._right = swap._left
        swap._left = self
        #reassign parents
        swap._parent = self._parent
        self._parent = swap
        return swap

    def rotate_right(self):
        #Carry out rotation on pointers
        swap = self._left
        self._left = swap._right
        swap._right = self
        #reassign parents
        swap._parent = self._parent
        self._parent = swap
        return swap

    def rebalance(self, v):
        bf = self.balance_factor()
        subtree_root = self
        if (bf > 1):
        #imbalance on the left => rebalance to the right
            print("imbalance on the left => rebalance to the right")
            if (v < self._left.value):
            #outside left imbalance
                print("outside case")
                subtree_root = self.rotate_right()
            else:
            #inside left imbalance
                print("inside case!")
                self._left = self._left.rotate_left() 
                subtree_root = self.rotate_right()
        elif (bf < -1):
        #imbalance on the right => rebalance to the left
            print("imbalance on the right => rebalance to the left")
            if (v > self._right.value):
            #outside right imbalance
                print("outside case")
                subtree_root = self.rotate_left()
            else:
            #inside right imbalance
                print("inside case!")
                self._right = self._right.rotate_right() 
                subtree_root = self.rotate_left()
        return subtree_root


    def add(self, v):
        # Reference to the newly added node
        # OR 
        # New subroot if rebalancing occurs on this node
        new_node = None

        #Added value creates a duplicate on this node  
        if (self.value == v):
            self.counter += 1
            return self
        
        #Value will be in a new node
        if (self.value > v):
        #Added value is smaller than node value => add to the left
            if (self._left == None):
            #No left child yet => create a new child node to hold v
                new_node = AVLNode(v)
                new_node._parent = self
                self._left = new_node
            else:
            #Call addition recursively on left child & rebalance
                self._left.add(v)
                self._left = self._left.rebalance(v)
                self._left._parent = self
        else:
        #Added value is larger than node value => add to the right
            if (self._right == None):
            #No right child yet => create a new child node to hold v
                new_node = AVLNode(v)
                new_node._parent = self
                self._right = new_node
            else:
            #Call addition recursively on right child & rebalance
                self._right.add(v)
                self._right = self._right.rebalance(v)
                self._right._parent = self
        
        return new_node
