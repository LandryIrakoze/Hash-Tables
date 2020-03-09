class DynamicArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

    def insert(self, index, value):

        if self.count >= self.capacity:
            self.double_size()
        
        if index > self.count:
            print('Error: Index out of range')

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(count, value)

    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]

        self.storage = new_storage


my_array = DynamicArray(4)
my_array.insert(0,1)
my_array.insert(0,2)
my_array.insert(1,3)
my_array.insert(3,4)
my_array.insert(0,5)
print(my_array.storage)