class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size 

    def _hash(self,key):
        hash = 0 

        for letter in key:
            hash = (hash + ord(letter) * 23) % len(self.data_map)

        return hash 
    
    def set(self,key,value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self, key):
        index = self._hash(key)

        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def print(self):
        for i, val in enumerate(self.data_map):
            print(i, ': ' ,val)

hash_table = HashTable()
hash_table.set('bolts',1400)
hash_table.set('washers',50)
hash_table.set('lumber',70)
print(hash_table.get_item('bolts'))
print(hash_table.get_item('lumber'))
print(hash_table.keys())
hash_table.print()