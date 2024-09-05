class UnsortedArray():

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.nb_elts = 0

    # Returns the number of elements stored in the array.
    def get_size(self):
        return self.nb_elts

    # Inserts a new element in the array.
    # Displays error notification if the array is already at full capacity.
    def insert(self, element):
        if self.nb_elts == self.capacity:
            print("Error: the array is at full capacity")
        else:
            self.array[self.nb_elts] = element
            self.nb_elts += 1


    # Removes an element from the array.
    # Displays error notification if the deleted value is not in the array.
    def delete(self, element):
        #HINT: start by finding the index of the value to remove
        index = self.find(element)
        if index:
            for j in range(index, self.nb_elts-1):
                self.array[j] = self.array[j+1]
            self.array[self.nb_elts - 1] = None
            self.nb_elts -= 1
        else:
            print("The value does not exist")


    # Returns the element at a given position in the array.
    # Returns None if there is no element yet at this position.
    def getElementAt(self, index):
        return self.array[index]

    # Uses LINEAR search to find the position of an element in the array.
    # Returns None if the searched value is not in the array.
    def find(self, element):
        for i in range(self.nb_elts):
            if self.array[i] == element:
                return i
            
        return None


    def display(self):
        print(self.nb_elts, 'values')
        print("[ ", end='')
        for i in range(self.nb_elts):
            print(self.array[i], end=' ')
        print("]")
