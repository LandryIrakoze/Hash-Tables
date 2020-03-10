import random

def longest_linked_list_chain(keys, buckets, loops=10):
    '''
    roll keys number of keys into buckets number of random buckets and count collisions
    '''
    for i in range(loops):
        key_counts = {}
        for i in range(buckets):
            key_counts[i] = 0
        for i in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1

            largest_n = 0
            for key in key_counts:
                if key_counts[key] > largest_n:
                    largest_n = key[key]

        print(f'Longest Linked List Chain for {keys} keys in {buckets} buckets (Load Factor: {keys/buckets:.2f}): {largest_n} ')


longest_linked_list_chain(500, 1000, 5)