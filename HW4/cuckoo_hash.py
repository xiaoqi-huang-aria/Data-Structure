import random


class Item():
    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __eq__(self, other):
        return self._key == other._key  # compare items based on their keys

    def __ne__(self, other):
        return not (self == other)  # opposite of __eq__

    def __lt__(self, other):
        return self._key < other._key  # compare items based on their keys


class CuckooHashTable():
    def __init__(self):
        self._size = 0
        self._maxsize = 11
        self._array1 = [None] * self._maxsize
        self._array2 = [None] * self._maxsize
        self._random1 = random.random()
        self._random2 = random.random()

    def _hash1(self, k):
        return hash((k, self._random1)) % self._maxsize

    def _hash2(self, k):
        return hash((k, self._random2)) % self._maxsize

    def __getitem__(self, k):
        """ given a key k, return the value associated with k
            use hash1/hash2 to compute the index
            raise KeyError if k does not exist in the table
        """
        # TODO
        if k not in self:
            raise KeyError(f'Key {k} not in the hash table')
        index1 = self._hash1(k)
        if self._array1[index1] is not None and self._array1[index1]._key == k:
            return self._array1[index1]._value
        index2 = self._hash2(k)
        if self._array2[index2] is not None and self._array2[index2]._key == k:
            return self._array2[index2]._value
        

    def __setitem__(self, k, v):
        """ if key k exists in either array, modify associated value to v
            if key k does not exist in both arrays, insert (k, v) into table as a new class Item
            if there's a cycle, rehash the table
            Hint: You may want to use the _resize function for cycles
        """
        # TODO
        item = Item(k, v)
        self._insert(item)

    def __delitem__(self, k):
        """ given a key k, set the corresponding index in self._array1 or self._array2 to None
            raise KeyError if k does not exist in the table
        """
        # TODO
        if k not in self:
            raise KeyError(f"Key {k} not in the hash table")
        index1 = self._hash1(k)
        if self._array1[index1] is not None and self._array1[index1]._key == k:
            self._array1[index1] = None
            self._size -= 1
            return
        index2 = self._hash2(k)
        if self._array2[index2] is not None and self._array2[index2]._key == k:
            self._array2[index2] = None
            self._size -= 1
            return

    def _resize(self):
        """ double the size of self._array1, self._array2.
            also self._maxsize
            Remember to rehash all the old (key, value) pairs!
        """
        # TODO
        old_array1 = self._array1
        old_array2 = self._array2
        self._maxsize *= 2
        self._array1 = [None] * self._maxsize
        self._array2 = [None] * self._maxsize
        self._size = 0
        self._random1 = random.random()
        self._random2 = random.random()
        for item in old_array1:
            if item is not None:
                self._insert(item)
        for item in old_array2:
            if item is not None:
                self._insert(item)
    
    def _insert(self, item, depth=0):
        if depth > self._maxsize:
            self._resize()
            self._insert(item)
            return
        index1 = self._hash1(item._key)
        if self._array1[index1] is None:
            self._array1[index1] = item
            self._size += 1
            return
        if self._array1[index1]._key == item._key:
            self._array1[index1]._value = item._value
            return
        item, self._array1[index1] = self._array1[index1], item
        index2 = self._hash2(item._key)
        if self._array2[index2] is None:
            self._array2[index2] = item
            self._size += 1
            return
        if self._array2[index2]._key == item._key:
            self._array2[index2]._value = item._value
            return
        item, self._array2[index2] = self._array2[index2], item
        self._insert(item, depth + 1)

    def __len__(self):
        # TODO
        return self._size

    def __contains__(self, k):
        """ return True if key k exists in the table
            return False otherwise
        """
        # TODO
        index1 = self._hash1(k)
        index2 = self._hash2(k)
        if self._array1[index1] and self._array1[index1]._key == k:
            return True
        if self._array2[index2] and self._array2[index2]._key == k:
            return True
        return False

    def __iter__(self):
        """ same as keys(self) """
        return self.keys()

    def keys(self):
        """ yield an generator of keys in table """
        def keys_generator():
            items = self.items()
            for item in items:
                yield item._key
            return keys_generator()

    def values(self):
        """ yield an generator of values in table """
        def values_generator():
            items = self.items()
            for item in items:
                yield item._value
        return values_generator()

    def items(self):
        """ yield an generator of Items in table """
        def items_generator():
            for i in self._array1:
                if i is not None:
                    yield i
            for i in self._array2:
                if i is not None:
                    yield i
        return items_generator()


def main():
    table = CuckooHashTable()
    for i in range(200):  # Tests __setitem__, insert 0 ~ 199. _resize() also need to work correctly.
        table[i] = "happy_coding"

    print(len(table))  # Tests __len__, should be 200.

    for j in range(195):  # Tests __delitem__, delete 0 ~ 194
        del table[j]

    print(len(table))  # Tests __len__, should be 5.

    for j in table.items():  # Tests items()
        print(j._key)  # 195, 196, 197, 198, 199 left in table

    print(table[196])  # Tests __getitem__
    # Should print "happy_coding"


if __name__ == "__main__":
    main()
