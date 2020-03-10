import hashlib
# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] != None:
            if self.storage[index].next == None:
                self.storage[index].next = LinkedPair(key, value)
            else:
                self.storage[index].next = LinkedPair(key, value)
                
        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if index < self.capacity and self.storage[index] != None:
            self.storage[index] = None
        else:
            print('key is not found')

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if index < self.capacity and self.storage[index] != None:
            return self.storage[index].value
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage.copy()
        self.capacity *= 2
        
        for bucket_item in old_storage:
            self.insert(bucket_item.key, bucket_item.value)
        # ht_copy = HashTable(self.capacity * 2)
        # self.capacity *= 2
        

if __name__ == "__main__":
    ht = HashTable(2)

    print(ht.storage)
    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    print(ht.storage)

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")


# ht1 = HashTable(8)

# ht1.insert("key-0", "val-0")
# ht1.insert("key-1", "val-1")
# ht1.insert("key-2", "val-2")
# ht1.insert("key-3", "val-3")
# ht1.insert("key-4", "val-4")
# ht1.insert("key-5", "val-5")
# ht1.insert("key-6", "val-6")
# ht1.insert("key-7", "val-7")
# ht1.insert("key-8", "val-8")
# ht1.insert("key-9", "val-9")

# return_value = ht1.retrieve("key-0")
# print(f'retrieve key-0 = {return_value}')
# return_value = ht1.retrieve("key-1")
# print(f'retrieve key-1 = {return_value}')
# return_value = ht1.retrieve("key-2")
# print(f'retrieve key-2 = {return_value}')
# return_value = ht1.retrieve("key-3")
# print(f'retrieve key-3 = {return_value}')
# return_value = ht1.retrieve("key-4")
# print(f'retrieve key-4 = {return_value}')
# return_value = ht1.retrieve("key-5")
# print(f'retrieve key-5 = {return_value}')
# return_value = ht1.retrieve("key-6")
# print(f'retrieve key-6 = {return_value}')
# return_value = ht1.retrieve("key-7")
# print(f'retrieve key-7 = {return_value}')
# return_value = ht1.retrieve("key-8")
# print(f'retrieve key-8 = {return_value}')
# return_value = ht1.retrieve("key-9")
# print(f'retrieve key-9 = {return_value}')