from UnsortedArray import UnsortedArray

class SortedArray(UnsortedArray):

    def __init__(self, capacity):
        super().__init__(capacity)


    # Inserts a new element in the array; the array remains sorted after insertion.
    # Displays error notification if the array is already at full capacity.
    def insert(self, element):
        print("inserting", element)
        if self.nb_elts == self.capacity:
            print("Array is full")
        else:
            i = self.nb_elts
            while i > 0 and self.array[i - 1] > element:
                self.array[i] = self.array[i - 1]
                i -= 1
            self.array[i] = element
            self.nb_elts += 1

    # Uses BINARY search to find the position of an element in the array.
    # Returns None if the searched value is not in the array.
    def find(self, element):
        low = 0
        high = self.nb_elts - 1
        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] == element:
                return mid
            elif self.array[mid] < element:
                low = mid + 1
            else:
                high = mid - 1
        return None
           


    def display(self):
        print(self.nb_elts, 'values')
        print("[ ", end='')
        for i in range(self.nb_elts):
            print(self.array[i], end=' ')
        print("]")
