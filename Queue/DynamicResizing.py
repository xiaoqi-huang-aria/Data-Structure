class DynamicCircularArrayQueue():
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, element):
        if self.is_full():
            self._resize(2 * self.capacity)
        self.array[self.tail] = element
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print('Error: Queue is empty')
            return None
        value = self.array[self.head]
        self.array[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1

        # When the array is quarter-full, the new array will be half full
        if 0 < self.size < self.capacity // 4:
            self._resize(self.capacity // 2)
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.array[self.head]

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[(self.head + i) % self.capacity]
        self.array = new_array
        self.capacity = new_capacity
        self.head = 0
        self.tail = self.size

    def __str__(self):
        s = str(self.size) + " values\n[ "
        i = self.head
        for j in range(self.size):
            s += str(self.array[i]) + " "
            i = (i + 1) % self.capacity
        s += "]"
        return s

# 示例使用
queue = DynamicCircularArrayQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)  # 输出: 4 values [ 1 2 3 4 ]
queue.enqueue(5)  # 触发扩展
print(queue)  # 输出: 5 values [ 1 2 3 4 5 ]
