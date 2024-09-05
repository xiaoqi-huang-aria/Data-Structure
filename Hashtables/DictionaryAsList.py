from DictionaryADT import DictionaryADT

class DictionaryAsDoubleList(DictionaryADT):

    """
    A DictionaryAsDoubleList (DADL) stores keys and values separately.
    It uses two Python lists of identical size: 
        _keys stores all the keys
        _values store all the values
    For any key-value pair (k, v) in the DADL, the index of k in _keys 
    corresponds to the index of v in _values.
    """
    def __init__(self):
        self._keys = []
        self._values = []

    def __len__(self):
        return len(self._keys)

    def __contains__(self, k):
        return (k in self._keys)

    def __iter__(self):
        self._iter = 0
        return self

    def __next__(self):
        if (self._iter >= len(self)):
            raise StopIteration
        else:
            k = self._keys[self._iter]
            self._iter += 1
            return k

    def __str__(self):
        s = "["
        for i in range(len(self)):
            s += "(" + str(self._keys[i]) + "," + str(self._values[i]) + ")"
        s += "]"
        return s


    """
    Inserts a new key-value pair in the DADL.
    """
    def put(self, k, v):
        if (k in self._keys):
            i = self._keys.index(k)
            self._values[i] = v
        else:
            self._keys.append(k)
            self._values.append(v)


    """
    Looks for a key-value pair whose key matches k in the DADL.
    Returns the value if k is a match in the DADL, None otherwise.
    """
    def get(self, k):
        if k in self._keys:
            i = self._keys.index(k)
            return self._values[i]
        return None


    """
    Looks for a key-value pair whose key matches k and removes it from the DADL.
    Returns the value if k is a match in the DADL, None otherwise.
    """
    def remove(self, k):
        if k in self._keys:
            i = self._keys.index(k)
            v = self._values[i]
            del self._keys[i]
            del self._values[i]
            return v
        return None


    """
    Deletes all the values in the DADL.
    """
    def clear(self):
        del self._keys[:]
        del self._values[:]