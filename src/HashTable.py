class HashTable():
    # A simple hash table implementation using chaining for collision resolution.
    # Data is stored as tuples inside the buckets where the first element of the tuple is the key.
    def __init__(self, size=10):
        # Initializes the hash table with a default size of 10 and creates empty buckets.
        self.size = size
        self.buckets = []
        for i in range(size):
            self.buckets.append([])

    def insert(self, data):
        # Inserts a tuple into the hash table. The first element of the tuple is used as the key.
        key = data[0]
        index = key % self.size
        for item in self.buckets[index]:
            if item[0] == key:
                self.buckets[index].remove(item)
                break
        self.buckets[index].append(data)

    def search(self, key):
        # Searches for a tuple in the hash table using the key. Returns the tuple if found, otherwise None.
        index = key % self.size
        for item in self.buckets[index]:
            if item[0] == key:
                return item
        return None



    




   