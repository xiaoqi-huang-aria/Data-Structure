class KVItem:
    """Lightweight composite to store key-value pairs as map items."""
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __eq__(self, other):
        return (self._key == other._key)

    def __ne__(self, other):
        return not (self == other)  # opposite of __eq__

    def __lt__(self, other):
        return self._key < other._key  # compare items based on their keys

    def __str__(self):
        return "(" + str(self._key) + "," + str(self._value) + ")"


