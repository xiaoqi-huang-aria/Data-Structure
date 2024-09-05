class DictionaryADT:

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __delitem__(self, key):
        return self.remove(key)

    """
    Inserts a new key-value pair (k,v) in the dictionary.
    """
    def put(self, k, v):
        pass


    """
    Looks for a key-value pair (K_i,V_i) whose key matches k in the dictionary.
    Returns the value V_i if K_i is found in the dictionary, None otherwise.
    """
    def get(self, k):
        pass


    """
    Looks for a key-value pair (K_i,V_i) whose key matches k in the dictionary.
    If there is no item whose key matches k, return None.
    Otherwise remove (K_i,V_i) from the dictionary and return V_i.
    """
    def remove(self, k):
        pass